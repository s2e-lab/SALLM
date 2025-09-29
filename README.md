[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/s2e-lab/multi-SALLM)


# Multi-SALLM: Security Assessment of Generated Code

This repository contains the code and data used in the paper "Multi-Sallm: A Multilingual Security Assessment of Generated Code".



## Dataset
The dataset used in this paper is available in the `Dataset` folder. The dataset contains 2,036 Python prompts that are security-centric. The JSONL file contains the following fields:
- `id`: The unique identifier of the prompt
- `technique`: The security technique that the prompt is based on
- `source`: The source of the prompt
- `prompt`: The prompt itself
- `insecure_code`: The insecure code snippet
- `language`: Prompt language
- `translated_prompt`: Translation in the corresponding language


## Loading the dataset of prompts from HuggingFace

The dataset is now published on HuggingFace. You can load it as follows:

```
from datasets import load_dataset
dataset = load_dataset("s2e-lab/multi-SALLM")
```


The corresponding source folder contains the test codes, requirements, and Docker file of the prompt.

## Generation
This folder contains the code used to generate the code snippets from the LLMs. The code is written in Python and uses the Huggingface Transformers library.
- `gpt_model.py`: This file contains the code used to generate the code snippets from the OpenAI models. The code is written in Python and uses the OpenAI API.
- `gemini_model.py`: This file contains the code used to generate the code snippets from the Gemini models. The code is written in Python and uses the Google Gemini API.
- `Huggingface_model.py`: This file contains the code used to generate the code snippets from the Huggingface models.

## Evaluation

- `run_tests.py`: Python script to run the docker tests for a python code. 
It can be configured to run the tests for the insecure solution on the Dataset. It can also be used to run the tests for generated code. 
- `codeql_job_runner.py`: Python script to run CodeQL.
- `pass_at_k.ipynb` and `pass_at_k_tests.ipynb`: jupyter notebooks to run the pass@k metric.

## Translation
- `translate_dataset_gpt.ipynb`: Python script to translate the prompts
- `retranslate_dataset_gpt.py`: Python script to retranslate the prompts in English and calculate the Bert score.

## Abstract
As Large Language Models (LLMs) become increasingly integrated into software
engineers’ daily workflows, it is critical to ensure the code they generate is not
just functionally correct but also secure. While LLMs can boost developer pro-
ductivity, prior empirical studies have shown that they often produce insecure
code. This issue stems from two key factors. First, the datasets commonly used
to evaluate LLMs don’t accurately reflect real-world software engineering tasks
where security is a concern. Instead, they tend to focus on competitive pro-
programming problems or classroom-style exercises, which lack the complexity and
security risks of production code integrated into larger systems. Second, current
evaluation metrics mostly emphasize functional correctness and overlook security-
rity aspects altogether. To address these gaps, we introduce Multi-Sallm, a
benchmarking framework designed to systematically evaluate LLMs’ ability to
generate secure code. The framework includes three main components: (1) a novel
dataset of security-focused Python prompts translated into 23 natural languages,
(2) configurable assessment techniques for analyzing generated code, and (3) new
metrics that assess models from the perspective of secure code generation.


## Citation
If you use this code or dataset in your research, please cite the following paper:
```
@misc{siddiq2025multi,
  title        = {Multi-Sallm: A Multilingual Security Assessment of Generated Code},
  author       = {Siddiq, Mohammed Latif and Ulfat, Noshin and Raihan, Nishat and Santos, Joanna C. S. and Zampieri, Marcos},
  year         = {2025},
  howpublished = {Manuscript},
  note         = {Preprint},
}

```

