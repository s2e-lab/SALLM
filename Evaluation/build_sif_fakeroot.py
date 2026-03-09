"""
build_sif_fakeroot.py

Builds Apptainer .sif images directly on the HPC (no Docker needed).
Uses `apptainer build --fakeroot` with generated .def files.

Python strategy: one SIF per item, bootstrapped from docker://python:3.10-slim.

Java strategy (two-stage to avoid re-downloading Maven deps 25×):
  Stage 1 — build sallm-java-base.sif:
    • Bootstraps from docker://maven:3.8.6-openjdk-8-slim
    • Copies pom.xml into the image
    • Runs `mvn dependency:go-offline` to bake all deps at /app/.m2
  Stage 2 — build one SIF per item from the local base:
    • Bootstraps from localimage (sallm-java-base.sif)
    • Copies only the item's .java source + test file
    • Runscript: `mvn test -Dmaven.repo.local=/app/.m2`

Run from the Evaluation/ directory:
    python build_sif_fakeroot.py [--lang python|java] [--force] [--debug] [--jobs N]
"""

import os
import sys
import subprocess
import shutil
import argparse
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import (
    PYTHON_DATASET_PATH, JAVA_DATASET_PATH,
    GITHUB_PYTHON_DATASET_PATH, GITHUB_JAVA_DATASET_PATH,
    SIF_DIR,
)

APPTAINER_BIN = shutil.which("apptainer") or shutil.which("singularity")
GITHUB_PYTHON_DIR = os.path.join(GITHUB_PYTHON_DATASET_PATH, "GitHub")
GITHUB_JAVA_DIR   = os.path.join(GITHUB_JAVA_DATASET_PATH, "src", "main", "java", "com", "sallm", "GitHub", "GitHub")
GITHUB_JAVA_TEST_DIR = os.path.join(GITHUB_JAVA_DATASET_PATH, "src", "test", "java", "com", "sallm", "GitHub", "GitHub")
JAVA_BASE_SIF     = os.path.join(SIF_DIR, "sallm-java-base.sif")


# ---------------------------------------------------------------------------
# Python
# ---------------------------------------------------------------------------

def make_python_def(item_id, dataset_dir, requirements_path, test_runner_path):
    """Generate Apptainer .def content for a Python test image."""
    source_path = os.path.join(dataset_dir, f"{item_id}.py")
    test_path   = os.path.join(dataset_dir, f"test_{item_id}.py")
    test_mod    = f"test_{item_id}"
    return f"""\
Bootstrap: docker
From: python:3.10-slim

%files
    {requirements_path} /prompt/requirements.txt
    {source_path} /prompt/{item_id}.py
    {test_path} /prompt/{test_mod}.py
    {test_runner_path} /prompt/test_runner.py

%post
    pip install --no-cache-dir -r /prompt/requirements.txt

%runscript
    cd /prompt && exec python test_runner.py {test_mod} "$@"
"""


def collect_python_entries():
    """Return list of build entries for Python GitHub items."""
    entries = []
    if not os.path.isdir(GITHUB_PYTHON_DIR):
        print(f"Warning: {GITHUB_PYTHON_DIR} not found, skipping Python.")
        return entries

    req_path         = os.path.join(GITHUB_PYTHON_DIR, "requirements.txt")
    test_runner_path = os.path.join(GITHUB_PYTHON_DIR, "test_runner.py")

    for fname in sorted(os.listdir(GITHUB_PYTHON_DIR)):
        if not fname.endswith("_Dockerfile"):
            continue
        item_id  = fname.replace("_Dockerfile", "")
        sif_name = f"sallm-py-{item_id}.sif".lower()
        entries.append({
            "item_id":     item_id,
            "lang":        "python",
            "dataset_dir": GITHUB_PYTHON_DIR,
            "req_path":    req_path,
            "runner_path": test_runner_path,
            "sif_path":    os.path.join(SIF_DIR, sif_name),
        })
    return entries


# ---------------------------------------------------------------------------
# Java
# ---------------------------------------------------------------------------

def make_java_base_def(pom_path):
    """Generate .def for the shared Java base image with Maven deps baked in."""
    src_pkg  = "com/sallm/GitHub/GitHub"
    return f"""\
Bootstrap: docker
From: maven:3.8.6-openjdk-8-slim

%setup
    mkdir -p $SINGULARITY_ROOTFS/app/src/main/java/{src_pkg}
    mkdir -p $SINGULARITY_ROOTFS/app/src/test/java/{src_pkg}
    mkdir -p $SINGULARITY_ROOTFS/app/target/surefire-reports

%files
    {pom_path} /app/pom.xml

%post
    cd /app && mvn dependency:go-offline -B --fail-never -Dmaven.repo.local=/app/.m2

%runscript
    cd /app && exec mvn test -Dmaven.repo.local=/app/.m2 "$@"
"""


def make_java_item_def(item_id, source_java_path, test_java_path):
    """Generate .def for a per-item Java SIF, bootstrapped from the base SIF."""
    src_pkg  = "com/sallm/GitHub/GitHub"
    return f"""\
Bootstrap: localimage
From: {JAVA_BASE_SIF}

%files
    {source_java_path} /app/src/main/java/{src_pkg}/{item_id}.java
    {test_java_path}   /app/src/test/java/{src_pkg}/Test{item_id}.java

%runscript
    cd /app && exec mvn test -Dmaven.repo.local=/app/.m2 "$@"
"""


def collect_java_entries():
    """Return list of build entries for Java GitHub items."""
    entries = []
    if not os.path.isdir(GITHUB_JAVA_DIR):
        print(f"Warning: {GITHUB_JAVA_DIR} not found, skipping Java.")
        return entries

    pom_path = os.path.join(GITHUB_JAVA_DATASET_PATH, "pom.xml")

    for fname in sorted(os.listdir(GITHUB_JAVA_DIR)):
        if not fname.endswith("_Dockerfile"):
            continue
        item_id      = fname.replace("_Dockerfile", "")
        source_path  = os.path.join(GITHUB_JAVA_DIR, f"{item_id}.java")
        test_path    = os.path.join(GITHUB_JAVA_TEST_DIR, f"Test{item_id}.java")
        sif_name     = f"sallm-java-{item_id}.sif".lower()
        entries.append({
            "item_id":     item_id,
            "lang":        "java",
            "pom_path":    pom_path,
            "source_path": source_path,
            "test_path":   test_path,
            "sif_path":    os.path.join(SIF_DIR, sif_name),
        })
    return entries


def build_java_base(force=False, debug=False):
    """Build the shared Java base SIF. Returns (ok, reason)."""
    if os.path.exists(JAVA_BASE_SIF) and not force:
        return True, "already exists"

    pom_path = os.path.join(GITHUB_JAVA_DATASET_PATH, "pom.xml")
    if not os.path.exists(pom_path):
        return False, f"pom.xml not found at {pom_path}"

    def_content = make_java_base_def(pom_path)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".def", delete=False,
                                     prefix="sallm_java_base_") as f:
        f.write(def_content)
        def_path = f.name

    stdout = None if debug else subprocess.DEVNULL
    stderr = None if debug else subprocess.DEVNULL
    os.makedirs(SIF_DIR, exist_ok=True)
    try:
        result = subprocess.run(
            [APPTAINER_BIN, "build", "--fakeroot", "--ignore-fakeroot-command",
             JAVA_BASE_SIF, def_path],
            stdout=stdout, stderr=stderr,
        )
        if result.returncode != 0:
            return False, "apptainer build (java base) failed"
        return True, "built"
    finally:
        os.unlink(def_path)


# ---------------------------------------------------------------------------
# Generic build
# ---------------------------------------------------------------------------

def build_one(entry, force=False, debug=False):
    """Build a single per-item SIF image. Returns (ok, reason)."""
    sif_path = entry["sif_path"]
    if os.path.exists(sif_path) and not force:
        return True, "already exists"

    if not APPTAINER_BIN:
        return False, "apptainer/singularity not found"

    if entry["lang"] == "python":
        def_content = make_python_def(
            entry["item_id"], entry["dataset_dir"],
            entry["req_path"], entry["runner_path"],
        )
    elif entry["lang"] == "java":
        if not os.path.exists(JAVA_BASE_SIF):
            return False, f"Java base SIF missing: {JAVA_BASE_SIF}"
        def_content = make_java_item_def(
            entry["item_id"], entry["source_path"], entry["test_path"],
        )
    else:
        return False, f"unsupported lang: {entry['lang']}"

    with tempfile.NamedTemporaryFile(mode="w", suffix=".def", delete=False,
                                     prefix=f"sallm_{entry['item_id']}_") as f:
        f.write(def_content)
        def_path = f.name

    stdout = None if debug else subprocess.DEVNULL
    stderr = None if debug else subprocess.DEVNULL

    # Java per-item SIFs use localimage bootstrap with no %post,
    # so --ignore-fakeroot-command avoids the fakeroot-lib issue in the Maven image.
    extra_flags = ["--ignore-fakeroot-command"] if entry["lang"] == "java" else []

    try:
        os.makedirs(SIF_DIR, exist_ok=True)
        result = subprocess.run(
            [APPTAINER_BIN, "build", "--fakeroot"] + extra_flags + [sif_path, def_path],
            stdout=stdout, stderr=stderr,
        )
        if result.returncode != 0:
            return False, "apptainer build failed"
        return True, "built"
    finally:
        os.unlink(def_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def _run_builds(entries, jobs, force, debug):
    success, skipped, failed = 0, 0, 0

    def _handle(ok, reason, item_id):
        nonlocal success, skipped, failed
        if ok:
            if reason == "already exists":
                skipped += 1
            else:
                success += 1
        else:
            failed += 1
            print(f"\nFAILED: {item_id} — {reason}")

    if jobs == 1:
        for entry in tqdm(entries, desc="Building"):
            ok, reason = build_one(entry, force=force, debug=debug)
            _handle(ok, reason, entry["item_id"])
    else:
        with ThreadPoolExecutor(max_workers=jobs) as pool:
            futures = {pool.submit(build_one, e, force, debug): e for e in entries}
            for fut in tqdm(as_completed(futures), total=len(futures), desc="Building"):
                entry = futures[fut]
                try:
                    ok, reason = fut.result()
                except Exception as exc:
                    ok, reason = False, str(exc)
                _handle(ok, reason, entry["item_id"])

    return success, skipped, failed


def main():
    parser = argparse.ArgumentParser(
        description="Build Apptainer SIF images for SALLM evaluation (no Docker required)."
    )
    parser.add_argument("--lang", choices=["python", "java"], default="python")
    parser.add_argument("--force", action="store_true",
                        help="Rebuild even if .sif already exists")
    parser.add_argument("--debug", action="store_true",
                        help="Show apptainer build output")
    parser.add_argument("--jobs", type=int, default=2,
                        help="Parallel build jobs (default: 2 for Python; use 1 for Java to avoid localimage race conditions)")
    args = parser.parse_args()

    if not APPTAINER_BIN:
        print("ERROR: apptainer/singularity not found in PATH.")
        sys.exit(1)

    os.makedirs(SIF_DIR, exist_ok=True)

    if args.lang == "python":
        entries = collect_python_entries()
        if not entries:
            print("No Python entries found.")
            sys.exit(1)
        print(f"Building {len(entries)} Python SIF images → {SIF_DIR}")
        s, sk, f = _run_builds(entries, args.jobs, args.force, args.debug)
        print(f"\nDone. Built: {s}, Skipped: {sk}, Failed: {f}")

    elif args.lang == "java":
        entries = collect_java_entries()
        if not entries:
            print("No Java entries found.")
            sys.exit(1)

        # Stage 1: base SIF
        print(f"Stage 1: Building shared Java base SIF ({JAVA_BASE_SIF}) ...")
        ok, reason = build_java_base(force=args.force, debug=args.debug)
        if not ok:
            print(f"ERROR building Java base SIF: {reason}")
            sys.exit(1)
        print(f"  → {reason}")

        # Stage 2: per-item SIFs
        print(f"Stage 2: Building {len(entries)} Java item SIF images ...")
        s, sk, f = _run_builds(entries, args.jobs, args.force, args.debug)
        print(f"\nDone. Built: {s}, Skipped: {sk}, Failed: {f}")

    if args.lang in ("python", "java"):
        print(f"SIF images in: {SIF_DIR}")


if __name__ == "__main__":
    main()
