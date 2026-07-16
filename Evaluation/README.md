# Evaluation Pipeline

Scripts to assess LLM-generated code (from [`../Generation/Filtered_Output/`](../Generation/README.md)) for
**functional correctness** and **security**, using two complementary techniques — test-based (sandboxed unit
tests) and static (CodeQL) — and to compute `pass@k`, `vulnerable@k`, and `secure@k`.

## Setup & dependencies

```bash
pip install -r requirements.txt
```
Non-Python tools, depending on which stage you run:
- **Docker** *or* **Apptainer/Singularity** — to sandbox test execution (Python/Java).
- **`g++`** (C++17) — to compile generated C++ against GoogleTest, and for the CodeQL C++ database build step.
- **JDK 8+ and Maven** — Java test execution base images use `maven:3.8.6-openjdk-8-slim`.
- **[CodeQL CLI](https://codeql.github.com/)** + a local clone of the
  [`github/codeql`](https://github.com/github/codeql) query-pack repo — only needed for the static-assessment
  pipeline (§3); not needed to just post-process existing CodeQL CSVs with `aggregate_codeql.py`.

`config.py` centralizes all paths (dataset locations, `Generation/Filtered_Output`, `TestResults/`, `sif_images/`)
relative to the repo root — read it before changing directory layout.

## Directory structure

- `Filtered_Output/` — *(actually lives in `../Generation/Filtered_Output/`)* input generations.
- `TestResults/` — annotated per-sample pass/fail output of the test-based pipeline (git-ignored; regenerate).
- `CodeQL_Output/<model>_<temp>/` — raw per-CWE CodeQL CSVs (§3).
- `Result/` — final aggregated CSVs consumed by [`../Result_Generation/`](../Result_Generation/README.md) (§4).
- `sif_images/` — pre-built Apptainer/Singularity images (§2), git-ignored.

## 1. Test-based assessment

Each prompt's test suite has (at least) a functional-correctness test method and a security test method; a sample
is "vulnerable" if its security test fails (Python/Java) — see [`../Dataset/README.md`](../Dataset/README.md) and
[`../DatasetJava/README.md`](../DatasetJava/README.md) for the exact test semantics.

### `run_tests_singularity.py` — the maintained runner (Python, Java, **and C++**)

```bash
python3 run_tests_singularity.py --model gpt --lang Python --no-github
python3 run_tests_singularity.py --model gemini --lang cpp --no-github
python3 run_tests_singularity.py --lang Python --github          # all models, GitHub-derived dataset
```
Flags: `--model` (`gpt`|`gemini`|`qwen2.5`|`starcoder2`, omit for all), `--lang` (`Python`|`Java`|`cpp`),
`--github`/`--no-github` (standard vs. CVE-derived dataset), `--test-mode` (small subset, for smoke-testing).

- **Python/Java**: runs each candidate inside a pre-built Apptainer/Singularity `.sif` image (see §2) — rootless,
  no Docker/no `sudo` required, suited to shared HPC systems.
- **C++**: no container — copies the generated `.cpp` plus the matching
  `DatasetCPP/test/<technique>/test_<id>.cpp` into a scratch dir, compiles with
  `g++ -std=c++17 ... -lgtest -lgtest_main -lpthread`, runs the binary with
  `--gtest_output=xml:results.xml`, and parses the GoogleTest XML. This is why
  [`../DatasetCPP/`](../DatasetCPP/README.md) must be built once first (`cmake --build build`) — the prebuilt
  `libgtest.a`/`libgtest_main.a` under `DatasetCPP/build/lib/` are reused here.

Results land in `TestModelsResults[_GitHub][_<Lang>]/temp_<T>/Model_..._results.csv`.

### `run_tests.py` — Docker-based runner (⚠ currently broken)

`run_tests.py` implements the same idea over plain Docker (build-once-per-prompt base image + volume-mounted
candidates + parallel `ProcessPoolExecutor`), documented via its `DEBUG` / `MAX_WORKERS` /
`RUN_TESTS_ON_GENERATED_CODE` / `TEST_MODE` flags at the top of the file. **As currently checked in, it fails at
import time**: it imports `TEMP_PATH` and `TEST_MODEL_RESULTS` from `config.py`, but `config.py` no longer defines
either name (confirmed by inspection — `config.py` only exports `BASE_DIR, ROOT_DIR, PYTHON_DATASET_PATH,
GITHUB_PYTHON_DATASET_PATH, GITHUB_JAVA_DATASET_PATH, CPP_DATASET_PATH, GENERATED_CODE_PATH, TEST_RESULTS,
JAVA_DATASET_PATH, TEST_FOLDER, SIF_DIR`). If you want to use the Docker path, add the two missing constants to
`config.py` (mirroring how `run_tests_singularity.py`'s own `_compute_paths()` derives them: `TEMP_PATH =
os.path.join(BASE_DIR, "temp")`, `TEST_MODEL_RESULTS = os.path.join(BASE_DIR, "TestModelsResults")`) before
running it. Otherwise, prefer `run_tests_singularity.py`.

### Post-processing

```bash
python3 run_test_evaluation.py     # annotate TestModelsResults*/ -> TestResults/*.jsonl (test_success/test_vulnerability)
python3 run_pass_at_k.py           # -> Result/Tests_Results_{Python,Java,Cpp}.csv (pass@k, vul@k, security@k)
```
`run_pass_at_k.py` merges the standard (100-prompt) and GitHub-derived (25-prompt) datasets for the same
model/temperature into 125 combined prompts, and uses the HumanEval unbiased `estimate_pass_at_k` estimator.
`Test_Evaluation.py`/`.ipynb` and `pass_at_k_tests.py` are earlier, superseded versions of these two steps
(Java-only / no C++ support) — kept for reference, not part of the maintained path.

`check_dataset_tests.py` is a separate QA utility: after running the test harness against the **canonical**
(insecure) samples themselves (not generated code), it verifies each test class has exactly the expected two test
methods, that the functional test passes, and that the security test fails — i.e. that the reference solution is
confirmed both correct and vulnerable, as designed.

### Building `.sif` images (needed once, before `run_tests_singularity.py`)

Two ways to produce the Apptainer/Singularity images consumed by `run_tests_singularity.py`:

- **`build_sif_fakeroot.py`** — run **directly on the target machine/HPC** (no Docker required):
  ```bash
  python build_sif_fakeroot.py --lang python-dataset   # or: python | java | java-std
  ```
  For Java, it first builds one shared base image (`mvn dependency:go-offline` baked in) and then a per-item image
  `Bootstrap: localimage From: <base.sif>` on top of it — use `--jobs 1` for Java to avoid `localimage` build races
  (the default `--jobs 2` is fine for Python). `build_sif_java_std.sh` / `build_sif_python_dataset.sh` are the
  corresponding SGE launcher wrappers.
- **`build_sif_images.py`** — run on a machine with **both Docker and Apptainer** installed; builds a normal Docker
  image from each `*_Dockerfile` and converts it (`apptainer build <sif> docker-daemon://<tag>`), for transferring
  to an HPC cluster afterward. `--lang {python,java}`, `--source <name>`, `--force`, `--debug`.

## 2. Static-based assessment (CodeQL)

```bash
python3 codeql_job_runner.py --mode python          # or: java | java_sq | cpp_gpt | cpp_gemini | cpp_qwen | cpp_starcoder2
python3 aggregate_codeql.py                         # -> Result/CodeQL_Results-Multi_{Python,Java,Cpp}.csv
```
`--mode` is **required**; there is no "all languages" mode — run once per `--mode` value (the `codeql_*.sh` files
in this folder are SGE wrappers for exactly these calls, one per model/language group, e.g. `codeql_python_all.sh`
→ `--mode python`, `codeql_cpp_gpt.sh` → `--mode cpp_gpt`).

For each matching `../Generation/Filtered_Output/*.jsonl`, `codeql_job_runner.py` reconstructs full source files
from the `compilable`-flagged generations, then invokes a per-language template script
(`codeql_job_bk.sh` / `codeql_job_cpp_bk.sh` / `codeql_job_java_bk.sh`) that:
1. `codeql database create --language={python,java,cpp} ...` (Java uses buildless extraction; C++ needs an actual
   `g++ -fsyntax-only` build command since C++ database creation requires compiling).
2. `codeql database analyze` against each CWE query directory under your local `codeql-repo` checkout (~30 CWE
   packs for Python, ~44 for Java, 14 for C++), writing one CSV per CWE to `CodeQL_Output/<model>_<temp>/`.

**You must edit the hard-coded `codeql`-on-`PATH` and `codeql-repo` paths** in `codeql_job_bk.sh` /
`codeql_job_cpp_bk.sh` / `codeql_job_java_bk.sh` (currently pointing at the original author's cluster path,
`/groups/.../codeql-home/...`) before running this locally.

`aggregate_codeql.py` takes no arguments and needs no CodeQL install — it's pure post-processing: for each
generation, it searches the corresponding CSVs for a finding referencing that exact (reconstructed) filename,
tags it `direct` (same CWE as the prompt) vs. `indirect`, and computes `vul@k`/`security@k` (+ `in_vul@k`/
`in_security@k` for indirect findings) with the same unbiased estimator used for `pass@k`. It skips any
model/temperature/language combination whose CodeQL CSVs are all empty (job never ran), rather than reporting a
misleading 100%-secure result.

> **C++ caveat**: CodeQL's C++ query coverage here is much narrower (14 rules) than Python (~48) or Java (~44).
> Near-zero `vulnerable@k` for C++ under CodeQL reflects limited static-analysis coverage, not superior security —
> rely on the test-based results (§1) for C++ security conclusions.

## 3. Cluster launch pattern (`eval_*.sh`)

All `eval_*.sh` files are SGE jobs of the form
`python3 run_tests_singularity.py --model <m> --lang {cpp|Java} --github|--no-github`
(one job per model × language × {standard, GitHub-derived} combination), following the naming pattern
`eval_{model}_{cpp|java}.sh` / `eval_{model}_github_{cpp|java}.sh`. `eval_python_all.sh` runs both dataset variants
for all models in one job. After all `eval_*.sh` jobs finish, `eval_notebooks_cpp.sh` / `eval_notebooks_java.sh`
chain the full aggregation: `run_test_evaluation.py` → `run_pass_at_k.py` → `column_k_evaluation.py` →
`analyze_compilability_result.py` → (Java only) `compare_python_java.py` → `aggregate_codeql.py` → the
`../Result_Generation/generate_*_figures.py` scripts. This is the canonical end-to-end order to reproduce
`Evaluation/Result/` and the paper's figures from scratch. As with `Generation/`'s job scripts, these are
cluster-specific (hard-coded `/groups/...` paths) — use them as a reference for argument combinations, not as
portable shell scripts.

## 4. Metrics & result tables (`Evaluation/Result/`)

| Script | Produces | Notes |
|---|---|---|
| `run_pass_at_k.py` | `Tests_Results_{Python,Java,Cpp}.csv` | `Model, Temp, Language(natural), pass@{1,3,5}, vul@{1,3,5}, security@{1,3,5}` |
| `aggregate_codeql.py` | `CodeQL_Results-Multi_{Python,Java,Cpp}.csv` | adds `in_vul@k`/`in_security@k` (indirect findings) |
| `analyze_compilability_result.py` | `compilation_results_{Python,Java,Cpp}.csv` | before/after-repair compilability rate |
| `column_k_evaluation.py` | `{Cpp,Java,Python}_{pass,vul,security}@{1,3,5}_mean_std_table.csv` | aggregated by the paper's 11 language families |
| `compare_python_java.py` | `Comparison_{pass,vul,security}@{1,3,5}_table.csv`, `Comparison_summary.csv` | Java-vs-Python head-to-head per family/model |

`CodeQL_Results-Multi.csv` and `compilation_results_multi.csv` (at the `Evaluation/` root, not `Result/`) are
older, undifferentiated-by-language artifacts predating the per-language split — superseded by the `Result/*`
files above, kept for provenance.

Interactive-notebook prototypes (`pass_at_k_codeql.ipynb`, `pass_at_k_tests.ipynb`, `repair_evaluation.ipynb`,
`CodeQL_Result_Analysis.ipynb`) preceded the flat scripts above (each script's own docstring says which notebook
it replaces) — the scripts are the maintained path. `ipynb_to_py.py` is the generic notebook→script extraction
utility used historically to bootstrap them.
