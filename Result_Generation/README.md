# Result_Generation

Turns the CSVs in [`../Evaluation/Result/`](../Evaluation/README.md) into the figures used in the paper.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Run from **inside `Result_Generation/`** (each script locates `../Evaluation/Result` relative to its own file
location), except `plot_language_family.py`, which writes to the relative path `Result_Generation/Figure` and must
therefore be run **from the repo root**:

```bash
cd Result_Generation
python3 generate_test_figures.py         # pass@k / vulnerable@k / security@k, from Tests_Results_*.csv
python3 generate_compilation_figures.py  # before/after-repair compilability, from compilation_results_*.csv
python3 generate_codeql_figures.py       # CodeQL vul@k / security@k, from CodeQL_Results-Multi_*.csv

cd ..
python3 Result_Generation/plot_language_family.py   # per-language-family pass@k / security@k trend figures
```

All figures are written to `Figure/` (88 PNGs, e.g. `nl_Cpp_pass_at_1.png`, `nl_Java_codeql_security_at_5.png`,
`lf_java_harder.png`, `lf_scaling_k.png`).

> **Note on `plot_language_family.py`**: its per-language-family, per-model numbers are a **hard-coded `DATA`
> dict** in the script itself, not read live from `Evaluation/Result/*.csv`. If the underlying result CSVs change,
> this script's numbers must be updated by hand to match — it does not regenerate itself from `Result/`.

## Other files

- `codeql_result.ipynb`, `compilation_rate.ipynb`, `tests_result.ipynb` — exploratory notebook precursors to the
  three `generate_*_figures.py` scripts above; kept for reference, not the maintained path.
