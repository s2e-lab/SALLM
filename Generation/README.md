# Generation

Scripts that call each of the 4 benchmarked LLMs to generate code for every prompt in
[`../ProcessedFiles/*_best.jsonl`](../Translation/README.md) (the translated-and-selected output of the
`Translation/` pipeline), across all 23 natural languages, 6 temperatures, and (nominally) 10 samples per
prompt/language/temperature — then repairs/cleans the raw output for downstream evaluation.

## Layout

```
Generation/
├── gpt_model.py            # GPT-4o-mini via OpenAI API
├── gemini_model.py         # Gemini-2.5-Flash via Google GenAI SDK
├── qwen_model.py           # Qwen2.5-Coder-3B-Instruct via Hugging Face's OpenAI-compatible router
├── Huggingface_model.py    # StarCoder2-3B, local inference (transformers, multi-GPU)
├── Ollama_model.py         # StarCoder2-3B via a local Ollama server (CPU/lighter-GPU alternative)
├── filter_code.py          # rule-based repair (R1–R4) + compilability check: Output/ -> Filtered_Output/
├── analyze_compilability.py
├── config.json              # NOT checked in (gitignored) — API keys, see below
├── Output/                  # raw generations, one .jsonl per (dataset, model, temperature)
├── Filtered_Output/         # repaired/cleaned generations (input to ../Evaluation/)
└── *.sh                     # SGE cluster job scripts (see "Cluster job scripts" below)
```

## Setup

```bash
pip install -r requirements.txt
```
(`torch`/`transformers` are only needed for `Huggingface_model.py`; use a CUDA-enabled `torch` build if you plan
to run it. `Ollama_model.py` additionally needs the [Ollama](https://ollama.com) binary on `PATH`, or let the
job scripts auto-download it. `filter_code.py`'s C++ compilability check shells out to `g++ -std=c++17`.)

Create `Generation/config.json`:
```json
{
  "OPENAI_KEY": "sk-...",
  "GEMINI_KEY": "...",
  "HF_TOKEN": "hf_..."
}
```
`gpt_model.py` only reads `OPENAI_KEY`; `gemini_model.py` only reads `GEMINI_KEY`; `qwen_model.py` only reads
`HF_TOKEN` (used against `https://router.huggingface.co/v1`). `Huggingface_model.py` and `Ollama_model.py` need no
config file (local inference).

## Running generation

Each script reads one input file (`../ProcessedFiles/<prefix>_nl_prompt_best.jsonl`, `<prefix>` ∈ `dataset`,
`dataset_java`, `dataset_cpp`, `github-dataset`, `github-dataset_java`, `github-dataset_cpp`) and internally loops
over **all 6 temperatures** and all languages present in the file, writing one output file per temperature to
`Output/`.

```bash
cd Generation
python3 gpt_model.py    ../ProcessedFiles/dataset_nl_prompt_best.jsonl
python3 gemini_model.py ../ProcessedFiles/dataset_nl_prompt_best.jsonl
python3 qwen_model.py   ../ProcessedFiles/dataset_nl_prompt_best.jsonl

# StarCoder2, local GPU inference (loops temps 0.2–1.0 only — see note below):
python3 Huggingface_model.py ../ProcessedFiles/dataset_nl_prompt_best.jsonl

# StarCoder2 via Ollama — one call per temperature (--temperature is required):
python3 Ollama_model.py ../ProcessedFiles/dataset_nl_prompt_best.jsonl --temperature 0.0
```

Output filename convention: `[github-]dataset[_java|_cpp]_nl_prompt_best_<model>_<temperature>.jsonl`, e.g.
`dataset_cpp_nl_prompt_best_gemini-2.5-flash_0.4.jsonl`, `github-dataset_java_nl_prompt_best_starcoder2_1.0.jsonl`.
The `github-`/`_java`/`_cpp` naming mirrors [`../Translation/`](../Translation/README.md)'s output naming.

**Sampling notes / known discrepancies from the paper's stated "10 samples":**
- `gpt_model.py` and `qwen_model.py` request `n=10` completions per call — matches.
- `gemini_model.py` requests `candidate_count=8` — Gemini-2.5-Flash generations therefore have **8**, not 10,
  raw samples per language/temperature before repair.
- `Huggingface_model.py` hard-codes `temperatures = [0.2, 0.4, 0.6, 0.8, 1.0]` (**no 0.0** — greedy/temp-0.0
  StarCoder2 samples are produced by `Ollama_model.py` instead, invoked separately per the job scripts).
- `Ollama_model.py` produces 10 sequential samples for `temperature > 0`, or exactly 1 for `temperature == 0.0`.

## Repair / filtering (`Output/` → `Filtered_Output/`)

```bash
python3 filter_code.py --model gpt        # or: gemini | qwen | starcoder2
python3 analyze_compilability.py --model gpt
```
`filter_code.py` implements the paper's rule-based repair:
- **R1** `extract_code_block` — pulls code out of ```` ``` ```` fences, handling unclosed/truncated fences.
- **R2** `remove_repetition` — strips echoed prompt text; for Java, also removes duplicate `import`/`package`/class
  declarations.
- **R3** (C++ only) — discards any `int main()` test harness the model appended after the target function/class.
- **R4** `fix_truncated_java` / `fix_truncated_cpp` — drops incomplete trailing lines and re-balances `{ }`; for
  Python, injects a `pass` if the code ends on a dangling block header.

It also strips model-specific sentinel tokens (StarCoder2), restores the real Java class name/`package` (undoing
the `ClassX` obfuscation from `../DatasetJava/`), and infers/prepends missing `#include`s for C++.
`check_compilable` uses `ast.parse` (Python), brace/keyword heuristics (Java), or `g++ -fsyntax-only` (C++), and
the result is written back as a `compilable: bool` flag alongside each sample's `cleared_code`.

> **Known gap:** `filter_code.py`'s `main()` currently only processes files whose name contains `"cpp"`. The
> Python/Java entries already present in `Filtered_Output/` were produced by an earlier/different version of this
> filtering logic (plausibly `Filtering.ipynb`, kept in this folder for reference). If you regenerate Python/Java
> `Filtered_Output/` files from scratch, you will need to adapt `filter_code.py`'s file-selection filter (or use
> `Filtering.ipynb` as a starting point) rather than relying on its current CLI as-is for those languages.

## Cluster job scripts

All `*.sh` files are **SGE** (Sun/Univa Grid Engine) job scripts from the original HPC cluster run
(`#$ -q ...`, `#$ -pe smp N`, hard-coded paths under `/groups/...`) — they are **not portable as-is**; use them as
a reference for the invocation pattern (one job per model × dataset/language combo) rather than running them
directly outside that cluster. The Ollama-specific jobs (`ollama_job*.sh`, `cpp_ollama*.sh`) additionally
auto-download a portable Ollama binary and manage a per-job local server/port.

## Other files

- `duplicate_outputs.py`, `merge_manual.py` — one-off historical recovery/patch scripts tied to specific past runs
  (e.g. backfilling a greedy temp-0.0 run to 10 samples, or re-merging orphaned multi-GPU shard files). Not part
  of the normal pipeline; kept for provenance.
- `test_filter.py`, `test_hf_api.py` — ad-hoc smoke-test scripts (not a pytest suite).
- `Filtering.ipynb`, `Token_Statistics.ipynb` — exploratory notebooks.
