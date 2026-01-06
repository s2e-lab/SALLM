# Translation Module

This module contains scripts to extract, translate, and evaluate prompts for the SALLM dataset. It uses OpenAI's GPT models for translation and BERTScore for quality evaluation via back-translation.

## Setup

1.  **Dependencies**: Install the required Python packages:
    ```bash
    pip install openai tqdm evaluate datasets bert_score transformers torch
    ```
2.  **Configuration**: Create a `config.json` file in this directory with your API keys:
    ```json
    {
      "OPENAI_KEY": "your_openai_api_key_here",
    }
    ```

## Pipeline Workflow

The translation process consists of three main steps. All generated files are stored in the `ProcessedFiles` directory.

### Step 1: Extract Docstrings
Extract natural language prompts (docstrings) from the code snippets in your dataset.
```bash
python3 Translation/extract_docstring_generalized.py <dataset_file.jsonl>
```
*Example*: `python3 Translation/extract_docstring_generalized.py Dataset/dataset.jsonl`

### Step 2: Generate Translation Candidates
Generate 10 translation candidates for each target language and immediately perform a back-translation for each.
```bash
python3 Translation/translate_dataset_gpt.py <extracted_file.jsonl> <docstring_key>
```
*Example*: `python3 Translation/translate_dataset_gpt.py ProcessedFiles/dataset_nl_prompt.jsonl prompt_nl_prompt`

### Step 3: Evaluate and Select Best Candidate
Use BERTScore to compare back-translations with the original English prompt and select the best version for each language.
```bash
python3 Translation/evaluate_translations.py <candidates_raw_file.jsonl> <docstring_key>
```
*Example*: `python3 Translation/evaluate_translations.py ProcessedFiles/dataset_nl_prompt_candidates_raw.jsonl prompt_nl_prompt`

## File Organization
- `extract_docstring_generalized.py`: Extracts docstrings from Python/Java.
- `translate_dataset_gpt.py`: Handles GPT-based translation (10 candidates) and back-translation.
- `evaluate_translations.py`: Selects the best translation based on BERTScore (using `distilbert-base-uncased`).
- `config.json`: Stores API credentials (ignored by git).