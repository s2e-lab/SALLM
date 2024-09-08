# SALLM: Security Assessment of Generated Code

This repository contains the code and data used in the paper "SALLM: Security Assessment of Generated Code" accepted to the 6th International Workshop on Automated and verifiable Software sYstem Development (ASYDE) Co-located with ASE 2024.

## Abstract
With the growing popularity of Large Language Models (LLMs) in software engineers’ daily practices, it is important to ensure that the code generated by these tools is not only functionally correct but also free of vulnerabilities. Although LLMs can help developers to be more productive, prior empirical studies have shown that LLMs can generate insecure code. There are two contributing factors to the insecure code generation. First, existing datasets used to evaluate LLMs do not adequately represent genuine software engineering tasks sensitive to security. Instead, they are often based on competitive programming challenges or classroom-type coding tasks. In real-world applications, the code produced is integrated into larger codebases, introducing potential security risks. Second, existing evaluation metrics primarily focus on the functional correctness of the generated code while ignoring security considerations. Therefore, in this paper, we described Sallm, a framework to benchmark LLMs’ abilities to generate secure code systematically. This framework has three major components: a novel dataset of security-centric Python prompts, configurable assessment techniques to evaluate the generated code, and novel metrics to evaluate the models’ performance from the perspective of secure code generation.


## Dataset
The dataset used in this paper is available in the `PythonDataset` folder. The dataset contains 100 Python prompts that are security-centric. The JSONL file contains the following fields:
- `id`: The unique identifier of the prompt
- `technique`: The security technique that the prompt is based on
- `source`: The source of the prompt
- `prompt`: The prompt itself
- `insecure_code`: The insecure code snippet
  
The corresponding source folder contains the test codes, requirement, and docker file of the prompt.

## Generation
This folder contains the code used to generate the code snippets from the LLMs. The code is written in Python and uses the Huggingface Transformers library.

## Evaluation
This folder contains the code used to evaluate the generated code snippets. The code is written in Python and uses the CodeQL library and Docker to run the code.

## Citation
If you use this code or dataset in your research, please cite the following paper:
```
@inproceedings{siddiq2024sallm,
  author={Siddiq, Mohammed Latif and Santos, Joanna C. S. and Devareddy, Sajith and Muller, Anna},
  title={SALLM: Security Assessment of Generated Code}, 
  booktitle = {Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW '24)},
  numpages = {12},
  location = {Sacramento, CA, USA},
  doi = {10.1145/3691621.3694934}
  series = {ASEW '24}
}
```

