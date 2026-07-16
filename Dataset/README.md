# Dataset (Python)

The original SALLM dataset: **100 security-centric Python prompts**, each pairing a function/method signature with
a known-*insecure* reference solution and unit tests that check both functional correctness and security.

For the 25 additional real-CVE-derived prompts, see [`../GitHubDataset/`](../GitHubDataset/README.md). For the
Java/C++ ports of these same 100 prompts, see [`../DatasetJava/`](../DatasetJava/README.md) and
[`../DatasetCPP/`](../DatasetCPP/README.md).

## Layout

```
Dataset/
├── Dataset_creator.ipynb     # builds dataset.jsonl from the per-sample .py files below
├── dataset.jsonl             # 100 entries — the compiled dataset (Git LFS)
├── prompt_cwe_mapping.csv    # id,cwe,prompt mapping used for CWE coverage analysis
├── Assertion/{Author,CWEList,CodeQL,SecurityEval,SonarSource,StackOverflow}/
├── Matching/{Author,CodeQL,StackOverflow}/         (+ codeql_job.sh)
└── Tainted/{Author,CodeQL,SecurityEval,StackOverflow}/  (+ codeql_job.sh)
```

`technique` (Assertion / Matching / Tainted) and `source` (Author / CodeQL / SecurityEval / SonarSource /
StackOverflow / CWEList) correspond to the two-level folder structure above. Each sample directory contains, per
prompt `<ID>`:
- `<ID>.py` — the insecure reference implementation (its docstring is the prompt)
- `test_<ID>.py` — unit test with (at least) a functional-correctness test method and a security test method
- `<ID>_Dockerfile`, `<ID>_requirements.txt` — the sandbox used to run the tests (see `../Evaluation/`)

## `dataset.jsonl` schema

```json
{
  "id": "Matching_Author_A_cwe502_0.py",
  "technique": "Matching",
  "source": "Author",
  "prompt": "...function signature + docstring...",
  "insecure_code": "...full reference solution...",
  "test_code": "...full unit test source..."
}
```
100 lines total (one per prompt). The multilingual, translated variant of `prompt` (`translated_prompt` +
`language`) is produced downstream by the [`Translation/`](../Translation/README.md) pipeline, not by this folder.

## Reproducing `dataset.jsonl` from source

```bash
cd Dataset
jupyter nbconvert --to notebook --execute Dataset_creator.ipynb   # writes dataset.jsonl in-place
```
The notebook walks the current directory for `*_cwe*.py` files (excluding `test_*.py`), and for each one derives
`id`/`technique`/`source` from its path, extracts the prompt as everything up to and including the file's last
`'''`-delimited docstring, and pulls in the matching `test_<file>` as `test_code`. No CLI arguments or external
API calls are needed — this step is fully offline.

## CWE coverage

`prompt_cwe_mapping.csv` lists the CWE-ID mapped to each prompt. Across Python/Java/C++ combined, the dataset
covers **45 distinct CWE identifiers** drawn from the MITRE Top 25 Most Dangerous Software Weaknesses plus
additional CWEs represented in CodeQL's and SonarSource's own rule documentation.

## Running CodeQL locally against the canonical (insecure) samples

`Matching/codeql_job.sh` and `Tainted/codeql_job.sh` run the CodeQL CLI against the reference (insecure) solutions
in each subfolder, one CWE query pack at a time. **Both scripts hard-code an author-local CodeQL install path**
(`/Users/codeql-home/codeql-repo/...`) — edit the `codeql database analyze` lines to point at your own checkout of
the [`github/codeql`](https://github.com/github/codeql) query-pack repo before running. This is a sanity-check
utility (confirming the canonical samples really do trip the expected CWE queries), not part of the main
generation→evaluation pipeline — see [`../Evaluation/README.md`](../Evaluation/README.md) for the pipeline used to
assess LLM-*generated* code.
