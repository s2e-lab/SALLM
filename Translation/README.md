# Translation Module

This module contains scripts to extract, translate, and retranslate prompts from the multi-SALLM dataset using GPT-4o-Mini via the OpenAI API. It supports multilingual benchmarking of software engineering tasks by enabling forward and back translation of prompts.



## Dataset
The dataset used in this module is available in the `Dataset` folder. The dataset contains Python functions and associated docstrings in multiple natural languages. The JSONL file incorporates two additional fields compared to the SALLM dataset:
- `language`: The language the prompt is translated into
- `translated_prompt`:  The translated prompt using the language mentioned in the "language" field

## Translation
This folder contains the code to extract the docstring from the prompt of the multi-SALLM dataset to translate and retranslate it to various natural languages.

- `extract_docstring_generalized.py`: This python file contains the code to extract docstrings from the provided dataset. It will produce a file with an additional entry containing the extracted docstring of the provided key.

- `translate_dataset_gpt.ipynb`: This notebook contains the code to translate the extracted docstring into one or more target languages. Configure your OpenAI API key and specify languages with their corresponding code in `language_translation_codes`. The language codes can be found in [flores](https://github.com/facebookresearch/flores/blob/main/flores200/README.md#languages-in-flores-200).

- `retranslate_dataset_gpt.py`: This file contains the code to retranslate the translated prompt back to English for evaluating translation using bertscore.