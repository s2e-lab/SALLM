# Translation Module

This module contains scripts to extract, translate, and evaluate prompts for the SALLM dataset. It uses OpenAI's GPT models for translation and BERTScore for quality evaluation via back-translation.

## Setup

1.  **Dependencies**: Install the required Python packages (`requirements.txt` only pins the scoring libraries —
    `openai`, `datasets`, and `torch` are also needed and are not pinned there):
    ```bash
    pip install -r requirements.txt
    pip install openai datasets transformers torch
    ```
2.  **Configuration**: Create a `config.json` file in this directory with your API key:
    ```json
    {
      "OPENAI_KEY": "your_openai_api_key_here"
    }
    ```

## Pipeline Workflow

The translation process consists of three main steps. All generated files are stored in the `../ProcessedFiles`
directory. **Run Step 1 from the repo root**; run Steps 2 and 3 from **inside `Translation/`** (`cd Translation`
first) — `extract_docstring_generalized.py` writes to the relative path `ProcessedFiles/`, while
`translate_dataset_gpt.py`/`evaluate_translations.py` write to `../ProcessedFiles` (with a same-directory
`ProcessedFiles/` fallback if the `../` path isn't found). Mixing up the working directory is the most common way
to get files written to the wrong place.

### Step 1: Extract Docstrings
Extract natural language prompts (docstrings) from the code snippets in your dataset. Takes two positional
arguments: the input file and the JSON key to write the extracted docstring under.
```bash
python3 Translation/extract_docstring_generalized.py <dataset_file.jsonl> <key>
```
*Example* (run from the repo root): `python3 Translation/extract_docstring_generalized.py Dataset/dataset.jsonl prompt`

### Step 2: Generate Translation Candidates
Generate 10 translation candidates for each target language and immediately perform a back-translation for each.
```bash
python3 translate_dataset_gpt.py <extracted_file.jsonl> <docstring_key>
```
*Example* (run from inside `Translation/`): `python3 translate_dataset_gpt.py ../ProcessedFiles/dataset_nl_prompt.jsonl prompt_nl_prompt`

### Step 3: Evaluate and Select Best Candidate
Use BERTScore to compare back-translations with the original English prompt and select the best version for each language.
```bash
python3 evaluate_translations.py <candidates_raw_file.jsonl> <docstring_key>
```
*Example* (run from inside `Translation/`): `python3 evaluate_translations.py ../ProcessedFiles/dataset_nl_prompt_candidates_raw.jsonl prompt_nl_prompt`

## File Organization
- `extract_docstring_generalized.py`: Extracts docstrings from Python/Java/C++.
- `translate_dataset_gpt.py`: Handles GPT-4o-mini translation (10 candidates) and back-translation.
- `evaluate_translations.py`: Selects the best translation by max BERTScore F1 (uses the library's default model,
  `roberta-large`; the smaller `distilbert-base-uncased` alternative is present in the code but commented out).
- `config.json`: Stores API credentials (ignored by git).
- `requirements.txt`: Pins `evaluate`, `bert-score`, `tqdm` — see Setup above for the rest.
- `job.sh` / `evaluate_job.sh`: SGE cluster job scripts (hard-coded to the original author's HPC path,
  `/groups/.../SALLM/Translation`) that run Steps 2 and 3 respectively — edit the `cd` path before reuse elsewhere.
- `create_eval_csv.py`: One-off script (hard-coded paths) that flattens a `*_best.jsonl` file into a CSV for manual
  human rating (naturalness/expressiveness/adequacy/conciseness) alongside the BERTScore numbers — this produced
  `Translation_Evaluation.csv` (blank rating columns) / `Translation_Evaluation_Scored.csv` (filled in), the
  human-evaluation instrument referenced by the paper's translation-quality validation.