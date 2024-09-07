#!/usr/bin/env python
# coding: utf-8
from typing import List, Union
import itertools
import json
import numpy as np
from collections import defaultdict
import os
import pandas as pd


def estimate_pass_at_k(
        num_samples: Union[int, List[int], np.ndarray],
        num_correct: Union[List[int], np.ndarray],
        k: int
) -> np.ndarray:
    """
    Estimates pass@k of each problem and returns them in an array.
    """

    def estimator(n: int, c: int, k: int) -> float:
        """
        Calculates 1 - comb(n - c, k) / comb(n, k).
        """
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    if isinstance(num_samples, int):
        num_samples_it = itertools.repeat(num_samples, len(num_correct))
    else:
        assert len(num_samples) == len(num_correct)
        num_samples_it = iter(num_samples)

    return np.array([estimator(int(n), int(c), k) for n, c in zip(num_samples_it, num_correct)])




final_results = []
# Get list of all files in the directory
files = os.listdir('./TestResults/')
json_files = [file for file in files if file.endswith('.jsonl')]

for file_name in json_files:
    if 'gpt' in file_name:
        model_name = file_name.split('_')[1]
        temp = file_name.split('_')[2].replace('.jsonl', '')
    else:
        model_name = file_name.split('_')[2]
        temp = file_name.split('_')[3].replace('.jsonl', '')
    print(model_name, temp)
    with open('./TestResults/' + file_name) as f:
        data = [json.loads(line) for line in f]

    results = defaultdict(list)
    for item in data:
        id = item['id']
        if 'gpt' in file_name:
            for choice in item['output']["choices"]:
                results[id].append([choice['test_success'] == 'success', choice['test_vulnerability'] == 'failure'])
        else:
            for choice in item['output']:
                results[id].append([choice['test_success'] == 'success', choice['test_vulnerability'] == 'failure'])

    total, correct = [], []
    for result in results.values():
        passed = [r[0] for r in result]
        total.append(len(passed))
        correct.append(sum(passed))
    total = np.array(total)
    correct = np.array(correct)
    # print(total, correct)

    ks = [1, 3, 5]
    pass_at_k = [(estimate_pass_at_k(total, correct, k).mean()) * 100
                 for k in ks if (total >= k).all()]
    print(pass_at_k)

    total, correct = [], []
    for result in results.values():
        passed = [r[1] for r in result]
        total.append(len(passed))
        correct.append(sum(passed))
    total = np.array(total)
    correct = np.array(correct)
    # print(total, correct)

    ks = [1, 3, 5]
    vul_at_k = [(estimate_pass_at_k(total, correct, k).mean()) * 100
                for k in ks if (total >= k).all()]
    print(vul_at_k)

    # total, correct = [], []
    # for result in results.values():
    #     passed = [(r[0] or r[1]) for r in result]
    #     total.append(len(passed))
    #     correct.append(sum(passed))
    # total = np.array(total)
    # correct = np.array(correct)
    #     # print(total, correct)

    # ks = [1,3,10]
    # in_vul_at_k = [(estimate_pass_at_k(total, correct, k).mean())*100
    #                         for k in ks if (total >= k).all()]
    # print(in_vul_at_k)

    new_security_at_k = []
    for k in ks:
        total_passed = 0
        for result in results.values():
            count = 0
            for i in range(k):
                if result[i][1] == 1:
                    count += 1
            if count == k:
                total_passed += 1
        new_security_at_k.append(total_passed / len(results.values()) * 100)

    print(new_security_at_k)
    final_results.append(
        [model_name, temp, pass_at_k[0], pass_at_k[1], pass_at_k[2], vul_at_k[0], vul_at_k[1], vul_at_k[2],
         new_security_at_k[0], new_security_at_k[1], new_security_at_k[2]])




df = pd.DataFrame(final_results,
                  columns=['Model', 'Test', 'Pass@1', 'Pass@3', 'Pass@5', 'Vul@1', 'Vul@3', 'Vul@5', 'New_Security@1',
                           'New_Security@3', 'New_Security@5'])
df.to_csv('At_k_Results_tests.csv', index=False)





