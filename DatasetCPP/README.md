# DatasetCPP

C++ port of the same 100 security-centric prompts as [`../Dataset/`](../Dataset/README.md), plus a 25-prompt
GitHub/CVE-derived set mirroring [`../GitHubDataset/`](../GitHubDataset/README.md). Each prompt preserves the
original task semantics and security context (same CWE, equivalent vulnerability pattern) as its Python and Java
([`../DatasetJava/`](../DatasetJava/README.md)) counterparts, enabling cross-language comparison.

## Layout

```
DatasetCPP/
├── DatasetCPP_creator.py       # -> DatasetCPP.jsonl        (100 entries: Assertion/Matching/Tainted)
├── generate_cpp_jsonl.py       # -> GitHubDatasetCPP.jsonl  (25 entries: GitHub/CVE-derived)
├── DatasetCPP.jsonl                    # Git LFS
├── GitHubDatasetCPP.jsonl              # Git LFS
├── CMakeLists.txt              # GoogleTest-based build for src/ + test/
├── src/{Assertion,Matching,Tainted,GitHub}/*.cpp     # insecure reference implementations
└── test/{Assertion,Matching,Tainted,GitHub}/test_*.cpp   # GoogleTest test cases
```

## `DatasetCPP.jsonl` / `GitHubDatasetCPP.jsonl` schema

```json
{
  "id": "A_cwe020_0.cpp",
  "technique": "Assertion",
  "source": "Author",
  "prompt": "...class + method signature + doc comment...",
  "insecure_code": "...full .cpp source...",
  "test_code": "...full GoogleTest source..."
}
```
`technique` ∈ {Assertion, Matching, Tainted} (or fixed `"GitHub"` for `GitHubDatasetCPP.jsonl`); `source` is derived
from the filename prefix (`A`→Author, `codeql`→CodeQL, `SE`→SecurityEval, `SO`→StackOverflow, `SS`→SonarSource,
`Mitre`→Mitre). Since C++ has no docstring convention, the prompt is extracted heuristically — everything up to and
including the class's documented method signature (falling back to "first `{(` line after the class declaration"
if no doc comment is found).

## Reproducing the dataset from source

```bash
cd DatasetCPP
python3 DatasetCPP_creator.py     # -> DatasetCPP.jsonl (100 entries)
python3 generate_cpp_jsonl.py     # -> GitHubDatasetCPP.jsonl (25 entries)
```
No CLI arguments and no external API calls — both scripts are pure filesystem walks over `src/`/`test/`.

## Building and running the reference tests

Requires **CMake ≥ 3.14** and a **C++17** compiler. GoogleTest is fetched automatically via CMake's `FetchContent`
(needs network access on first configure, unless you provide an offline mirror).

```bash
cd DatasetCPP
cmake -S . -B build
cmake --build build
cd build && ctest      # or: ./runTests
```
This builds and runs the *canonical insecure* solutions' tests, to confirm the reference implementations behave as
documented. To evaluate LLM-*generated* C++ code (compiled against the matching `test/<technique>/test_<id>.cpp`
files), see [`../Evaluation/README.md`](../Evaluation/README.md) (`run_tests_singularity.py`'s `run_cpp_test`,
which links against the `libgtest.a`/`libgtest_main.a` produced by this same CMake build).
