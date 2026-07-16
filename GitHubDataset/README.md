# GitHubDataset

25 additional Python prompts derived from **real-world vulnerabilities** (CVEs and vulnerable GitHub code
patterns), complementing the 100 synthetic prompts in [`../Dataset/`](../Dataset/README.md). These were selected
because they (1) affect Python libraries/frameworks, (2) map to a CWE in the MITRE Top 25 Most Dangerous Software
Weaknesses, and (3) have a publicly observable vulnerable code pattern (NVD demonstrative example or GitHub commit)
that could be abstracted into a function-signature prompt.

For the Java counterpart, see [`../GitHubDatasetJava/`](../GitHubDatasetJava/README.md); for the C++ counterpart,
see the `src/GitHub/`/`test/GitHub/` subfolders under [`../DatasetCPP/`](../DatasetCPP/README.md).

## Layout

```
GitHubDataset/
├── cve_mapping.csv          # file,cwe,cve — the CVE each prompt was derived from
├── github-dataset.jsonl     # 25 entries (Git LFS)
└── GitHub/
    ├── GitHub_cwe<NNN>_<i>.py               # insecure reference implementation
    ├── test_GitHub_cwe<NNN>_<i>.py          # unit test (functional + security)
    ├── GitHub_cwe<NNN>_<i>_Dockerfile
    ├── requirements.txt                      # shared deps (Flask, requests, PyYAML, unittest-xml-reporting)
    └── test_runner.py
```

`cve_mapping.csv` covers CWE-020, 022, 078, 079, 089, 094, 116, 200, 295, 327, 400, 434, 502, 601, 611, 798, 918
across the 25 prompts.

## `github-dataset.jsonl` schema

```json
{
  "id": "GitHub_cwe020_0.py",
  "technique": "Refinement",
  "source": "GitHubDataset",
  "prompt": "...function signature + docstring...",
  "insecure_code": "...full reference solution...",
  "language": "Python"
}
```
**Note:** unlike `Dataset/dataset.jsonl`, this file does **not** inline a `test_code` field — the unit tests live
only as standalone `test_GitHub_cwe<NNN>_<i>.py` files under `GitHub/`. Anything consuming this dataset for
evaluation should read the test file directly from `GitHubDataset/GitHub/` (this is what
`Evaluation/config.py`'s `GITHUB_PYTHON_DATASET_PATH` points at).

## Reproducing `github-dataset.jsonl`

No generator script for this file exists in the current repository (unlike `DatasetCPP/generate_cpp_jsonl.py` or
`GitHubDatasetJava/generate_java_jsonl.py`) — it was produced from the per-sample `.py`/Dockerfile/`cve_mapping.csv`
inputs above via a process not retained in version control. If you need to regenerate it, the schema above and the
sibling generators (`DatasetCPP/generate_cpp_jsonl.py`, `GitHubDatasetJava/generate_java_jsonl.py`) are the closest
reference for the expected shape.
