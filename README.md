[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/s2e-lab/multi-SALLM)

# Multi-SALLM: A Multilingual Security Assessment of Generated Code

This repository contains the framework, dataset, and evaluation pipeline used in the paper
**"Multi-SALLM: A Multilingual Security Assessment of Generated Code"** (an extended version of the
[SALLM](https://doi.org/10.1145/3691621.3694934) ASEW'24 paper). MULTI-SALLM benchmarks how well LLMs
generate code that is **both functionally correct and secure**, across:

- **3 programming languages**: Python, Java, C++
- **23 natural languages** used to phrase the prompts (English + 22 translations, back-translation validated with BERTScore)
- **125 security-centric prompts per language** (100 curated from Stack Overflow / CWE / CodeQL / Sonar Rules examples + 25 mined from real CVEs/GitHub)
- **4 LLMs**: StarCoder2-3B, Qwen2.5-Coder-3B-Instruct, GPT-4o-mini, Gemini-2.5-Flash
- **6 sampling temperatures** (0.0–1.0, step 0.2), **10 samples per prompt**

It introduces two security-oriented metrics — **`secure@k`** and **`vulnerable@k`** — alongside the standard
**`pass@k`** functional-correctness metric, and evaluates generated code with both **test-based** (Docker/Apptainer
sandboxed unit tests) and **static** (CodeQL) assessment.

> **Note:** dataset/generation artifacts (`*.jsonl`) are tracked with **Git LFS**. Clone with LFS enabled
> (`git lfs install && git clone https://github.com/s2e-lab/SALLM.git -b multi-sallm`) or run `git lfs pull`
> after cloning, otherwise these files will only contain small LFS pointer stubs.

## Abstract

As Large Language Models (LLMs) become increasingly integrated into software engineers' daily workflows, it is
critical to ensure the code they generate is not just functionally correct but also secure. While LLMs can boost
developer productivity, prior empirical studies have shown that they often produce insecure code. This issue stems
from two key factors. First, the datasets commonly used to evaluate LLMs don't accurately reflect real-world
software engineering tasks where security is a concern — they tend to focus on competitive-programming problems or
classroom-style exercises. Second, current evaluation metrics mostly emphasize functional correctness and overlook
security altogether. To address these gaps, we introduce **Multi-SALLM**, a benchmarking framework that includes
(1) a novel dataset of security-focused Python, Java, and C++ prompts translated into 23 natural languages, (2)
configurable static/dynamic assessment techniques, and (3) two new metrics (`secure@k`, `vulnerable@k`) that assess
models from the perspective of secure code generation. Our empirical evaluation of four state-of-the-art LLMs
(StarCoder2, Qwen2.5-Coder, GPT-4o-mini, Gemini-2.5-Flash) reveals three key findings: **(1)** functional
correctness and security are related but not equivalent — the models with the highest `pass@k` also tend to have
the highest `vulnerable@k`; **(2)** the *target programming language* has a much stronger effect on results than
the *prompt's natural language* (Java is consistently the hardest target, C++ the easiest once compilation clears);
**(3)** *sampling strategy is a risk factor* — higher temperature and larger `k` increase the chance of a correct
solution but also increase `vulnerable@k` and sharply reduce `secure@k`.

## Repository Structure & Pipeline

The repository mirrors the framework's four stages end to end. Every stage folder has its own `README.md` with
exact, copy-pasteable commands — this section is the map between them.

```
Dataset/, DatasetCPP/, DatasetJava/,            1. DATASET CREATION
GitHubDataset/, GitHubDatasetJava/                 curated + CVE/GitHub-derived prompts (Python/Java/C++)
        │
        ▼
Translation/  ──────────────────────────────►   2. TRANSLATION
   extract docstrings → GPT-4o-mini translate       23 natural languages, back-translation + BERTScore
   (×10 candidates) → back-translate → BERTScore     selection → ProcessedFiles/*_nl_prompt_best.jsonl
   select best-of-10 per language
        │
        ▼
ProcessedFiles/  (intermediate translation outputs, consumed by Generation/)
        │
        ▼
Generation/  ────────────────────────────────►   3. CODE GENERATION + REPAIR
   gpt_model.py / gemini_model.py / qwen_model.py    4 models × 6 temperatures × 23 languages × 10 samples
   / Huggingface_model.py / Ollama_model.py           raw completions → Output/
   filter_code.py (rule-based repair, R1–R4)           cleaned + compilability-checked → Filtered_Output/
        │
        ▼
Evaluation/  ────────────────────────────────►   4. SECURITY & CORRECTNESS ASSESSMENT
   run_tests_singularity.py (test-based:              pass@k, vulnerable@k, secure@k
     Docker/Apptainer + unit tests, Python/Java/C++)
   codeql_job_runner.py + CodeQL CLI (static)
   run_pass_at_k.py, aggregate_codeql.py, etc.       → Evaluation/Result/*.csv
        │
        ▼
Result_Generation/  ─────────────────────────►   5. FIGURES
   generate_test_figures.py / generate_compilation_figures.py / generate_codeql_figures.py → Figure/*.png
```

| Folder | Purpose | README |
|---|---|---|
| `Dataset/` | Original 100 Python prompts (Assertion / Matching / Tainted techniques), + `Dataset_creator.ipynb` | [Dataset/README.md](Dataset/README.md) |
| `DatasetCPP/` | C++ port of the 100 prompts + CMake/GoogleTest build | [DatasetCPP/README.md](DatasetCPP/README.md) |
| `DatasetJava/` | Java port of the 100 prompts + Maven build | [DatasetJava/README.md](DatasetJava/README.md) |
| `GitHubDataset/`, `GitHubDatasetJava/` | 25 additional prompts derived from real CVEs/GitHub commits (Python, Java) | [GitHubDataset/README.md](GitHubDataset/README.md) |
| `Translation/` | Docstring extraction → GPT-4o-mini translation → BERTScore-based selection into 23 languages | [Translation/README.md](Translation/README.md) |
| `Generation/` | Per-model code generation scripts + rule-based repair/filtering | [Generation/README.md](Generation/README.md) |
| `Evaluation/` | Test-based (Docker/Apptainer) + static (CodeQL) assessment, metric computation | [Evaluation/README.md](Evaluation/README.md) |
| `Result_Generation/` | Turns `Evaluation/Result/*.csv` into the paper's figures | [Result_Generation/README.md](Result_Generation/README.md) |
| `ProcessedFiles/` | Intermediate translation-pipeline outputs (input to `Generation/`) | see [Translation/README.md](Translation/README.md) |
| `util-scripts/`, `scripts/` | One-off dataset/Docker maintenance utilities | inline comments in each script |

## Dataset

The prompt dataset is security-centric: each prompt is a function/method signature describing a task that has one
or more functionally-correct but potentially **insecure** solutions, paired with a known-insecure reference
solution and unit tests that check both *functional correctness* and *security*. Across Python/Java/C++ combined,
the dataset spans **45 distinct CWE identifiers** drawn from the MITRE Top 25 Most Dangerous Software Weaknesses,
CodeQL, and Sonar Rules.

Each `.jsonl` record (schema varies slightly per language — see the per-folder READMEs) generally includes:
- `id`, `technique` (Assertion/Matching/Tainted/GitHub), `source` (Author/CodeQL/SecurityEval/SonarSource/StackOverflow/GitHub)
- `prompt` — the function/method signature + docstring given to the model
- `insecure_code` — a reference solution that is functionally correct but vulnerable
- `test_code` — unit tests checking functional correctness *and* security (e.g. `test_functionality`, `test_security`)
- (multilingual variant) `language`, `translated_prompt` — the natural-language translation of the prompt

### Loading the (Python, English-only) dataset from Hugging Face

```python
from datasets import load_dataset
dataset = load_dataset("s2e-lab/multi-SALLM")
```

For the full multilingual (23 languages) × multi-programming-language (Python/Java/C++) dataset, use the files in
this repository directly (`Dataset/`, `DatasetCPP/`, `DatasetJava/`, `GitHubDataset*/`, and the translated prompts
under `ProcessedFiles/*_best.jsonl`) — see [Dataset/README.md](Dataset/README.md).

## Quickstart: reproducing an experiment end to end

Each stage's README has full details; this is the minimal path from prompts to metrics for **one** model/language:

```bash
git clone -b multi-sallm https://github.com/s2e-lab/SALLM.git && cd SALLM
git lfs pull   # materialize dataset/generation .jsonl files

# 1. (optional — already provided) regenerate the multilingual prompts
#    see Translation/README.md

# 2. generate code with a model (needs Generation/config.json with API keys, see Generation/README.md)
cd Generation
python3 gpt_model.py ../ProcessedFiles/dataset_nl_prompt_best.jsonl   # loops all 6 temperatures
python3 filter_code.py                                                # rule-based repair + compilability check

# 3. evaluate (test-based, requires Apptainer/Singularity or Docker; see Evaluation/README.md)
cd ../Evaluation
python3 run_tests_singularity.py --model gpt --lang Python --no-github
python3 run_test_evaluation.py
python3 run_pass_at_k.py     # -> Result/Tests_Results_Python.csv (pass@k, vul@k, security@k)

# 4. (optional) static assessment with CodeQL, see Evaluation/README.md
python3 codeql_job_runner.py --mode python
python3 aggregate_codeql.py  # -> Result/CodeQL_Results-Multi_Python.csv
```

**Requirements to run the full pipeline** (see per-folder READMEs for exact versions/pins):
Python 3.10+, Docker **or** Apptainer/Singularity, `g++` (C++17), JDK 8+ with Maven, and — only for the static
assessment — a local [CodeQL CLI](https://codeql.github.com/) install with the `github/codeql` query-pack repo
checked out. API keys are needed for `GPT-4o-mini` (`OPENAI_KEY`), `Gemini-2.5-Flash` (`GEMINI_KEY`), and
`Qwen2.5-Coder` when run through the Hugging Face inference router (`HF_TOKEN`); StarCoder2 can be run fully
locally (`Huggingface_model.py`, needs a GPU) or via [Ollama](https://ollama.com) (`Ollama_model.py`).

**Known environment-specific pieces** — several scripts across `Generation/`, `Evaluation/`, and `Translation/`
were run on the original authors' SGE-managed HPC cluster and contain hard-coded absolute paths / job-scheduler
directives (`#$ ...`). These are documented per-folder as **cluster job scripts**; the underlying Python scripts
they call are portable and take normal CLI arguments.

## Citation

If you use this framework or dataset in your research, please cite:

```bibtex
@article{siddiq2026multi,
  title     = {Multi-Sallm: A Multilingual Security Assessment of Generated Code},
  author    = {Siddiq, Mohammed Latif and Ulfat, Noshin and Raihan, Nishat and Santos, Joanna C. S. and Zampieri, Marcos},
  year      = {2026},
  journal   = {Automated Software Engineering, An International Journal},
  note      = {Accepted},
  url       = {https://lsiddiqsunny.github.io/public/multi_sallm.pdf},
}
```

This work extends our earlier workshop paper:

```bibtex
@inproceedings{siddiq2024sallm,
  title     = {Sallm: Security assessment of generated code},
  author    = {Siddiq, Mohammed Latif and Silva Santos, Joanna C. and Devareddy, Sandeep and Muller, Anna},
  booktitle = {Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering Workshops},
  pages     = {54--65},
  year      = {2024},
  doi       = {10.1145/3691621.3694934}
}
```

## License

Apache License 2.0 — see [LICENSE](LICENSE).
