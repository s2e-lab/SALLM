"""
build_sif_images.py

Run this script on a machine that has BOTH Docker and Apptainer/Singularity installed
(e.g., your local workstation or a build node with root).

It will:
  1. Build each Docker image from its Dockerfile
  2. Convert it to a .sif file using `apptainer build`
  3. Save the .sif files to ./sif_images/

Then copy/transfer the entire sif_images/ directory to the HPC cluster and set
SIF_DIR in run_tests_singularity.py to point to it.

Usage:
    python build_sif_images.py [--lang python|java] [--source GitHubDataset|Author|...]
"""

import os
import sys
import subprocess
import shutil
import argparse
from tqdm import tqdm
from config import PYTHON_DATASET_PATH, JAVA_DATASET_PATH, GITHUB_PYTHON_DATASET_PATH, GITHUB_JAVA_DATASET_PATH, SIF_DIR

DOCKER_BIN = shutil.which("docker")
APPTAINER_BIN = shutil.which("apptainer") or shutil.which("singularity")


def find_dockerfiles(lang_filter=None, source_filter=None):
    """Scan dataset directories for Dockerfiles and return build info."""
    entries = []

    # Python datasets
    if lang_filter is None or lang_filter.lower() == 'python':
        for dataset_dir, is_github in [
            (PYTHON_DATASET_PATH, False),
            (GITHUB_PYTHON_DATASET_PATH, True),
        ]:
            if not os.path.exists(dataset_dir):
                continue
            for root, dirs, files in os.walk(dataset_dir):
                for f in files:
                    if f.endswith('_Dockerfile'):
                        item_id = f.replace('_Dockerfile', '')
                        parts = root.split(os.sep)
                        if is_github:
                            source = parts[-1]
                            technique = parts[-2] if len(parts) >= 2 else "GitHub"
                        else:
                            source = parts[-1]
                            technique = parts[-2] if len(parts) >= 2 else "Assertion"

                        if source_filter and source_filter.lower() != source.lower():
                            continue

                        sif_name = f"sallm-py-{item_id}.sif".lower()
                        entries.append({
                            'item_id': item_id,
                            'technique': technique,
                            'source': source,
                            'is_python': True,
                            'dockerfile': os.path.join(root, f),
                            'context': root,
                            'image_tag': f"sallm-py-{item_id}".lower(),
                            'sif_path': os.path.join(SIF_DIR, sif_name),
                        })

    # Java datasets
    if lang_filter is None or lang_filter.lower() == 'java':
        for dataset_dir, is_github in [
            (JAVA_DATASET_PATH, False),
            (GITHUB_JAVA_DATASET_PATH, True),
        ]:
            if not os.path.exists(dataset_dir):
                continue
            for root, dirs, files in os.walk(dataset_dir):
                for f in files:
                    if f.endswith('_Dockerfile'):
                        item_id = f.replace('_Dockerfile', '')
                        parts = root.split(os.sep)
                        source = parts[-1]
                        technique = parts[-2] if len(parts) >= 2 else "GitHub"

                        if source_filter and source_filter.lower() != source.lower():
                            continue

                        context = GITHUB_JAVA_DATASET_PATH if is_github else root
                        sif_name = f"sallm-java-{item_id}.sif".lower()
                        entries.append({
                            'item_id': item_id,
                            'technique': technique,
                            'source': source,
                            'is_python': False,
                            'dockerfile': os.path.join(root, f),
                            'context': context,
                            'image_tag': f"sallm-java-{item_id}".lower(),
                            'sif_path': os.path.join(SIF_DIR, sif_name),
                        })

    return entries


def build_sif(entry, force=False, debug=False):
    stdout = sys.stdout if debug else subprocess.DEVNULL
    stderr = subprocess.STDOUT if debug else subprocess.DEVNULL

    sif_path = entry['sif_path']
    if os.path.exists(sif_path) and not force:
        return True, "already exists"

    if not DOCKER_BIN:
        return False, "docker not found"
    if not APPTAINER_BIN:
        return False, "apptainer/singularity not found"

    # Step 1: docker build
    result = subprocess.run(
        [DOCKER_BIN, "build", "-t", entry['image_tag'], "-f", entry['dockerfile'], entry['context']],
        stdout=stdout, stderr=stderr
    )
    if result.returncode != 0:
        return False, "docker build failed"

    # Step 2: apptainer build from local docker daemon
    os.makedirs(SIF_DIR, exist_ok=True)
    result = subprocess.run(
        [APPTAINER_BIN, "build", sif_path, f"docker-daemon://{entry['image_tag']}"],
        stdout=stdout, stderr=stderr
    )
    if result.returncode != 0:
        return False, "apptainer build failed"

    return True, "built"


def main():
    parser = argparse.ArgumentParser(description="Build Apptainer SIF images for SALLM evaluation.")
    parser.add_argument('--lang', choices=['python', 'java'], default=None, help="Filter by language")
    parser.add_argument('--source', default=None, help="Filter by source (e.g. GitHubDataset, Author)")
    parser.add_argument('--force', action='store_true', help="Rebuild even if SIF already exists")
    parser.add_argument('--debug', action='store_true', help="Show build output")
    args = parser.parse_args()

    if not DOCKER_BIN:
        print("ERROR: Docker not found. This script must be run on a machine with Docker installed.")
        sys.exit(1)
    if not APPTAINER_BIN:
        print("ERROR: Apptainer/Singularity not found. Install it or run on a machine that has it.")
        sys.exit(1)

    entries = find_dockerfiles(lang_filter=args.lang, source_filter=args.source)
    if not entries:
        print("No Dockerfiles found. Check your dataset paths.")
        sys.exit(1)

    print(f"Found {len(entries)} images to build. SIF output: {SIF_DIR}")
    os.makedirs(SIF_DIR, exist_ok=True)

    success, skipped, failed = 0, 0, 0
    for entry in tqdm(entries, desc="Building SIF images"):
        ok, reason = build_sif(entry, force=args.force, debug=args.debug)
        if ok:
            if reason == "already exists":
                skipped += 1
            else:
                success += 1
        else:
            failed += 1
            print(f"FAILED: {entry['item_id']} — {reason}")

    print(f"\nDone. Built: {success}, Skipped (already exist): {skipped}, Failed: {failed}")
    if failed == 0:
        print(f"Transfer {SIF_DIR}/ to the HPC cluster and set SIF_DIR in run_tests_singularity.py.")


if __name__ == "__main__":
    main()
