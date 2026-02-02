# %%
import json
import os
import subprocess
import shutil

# %%
# Get list of all files in the directory
files = os.listdir('../Generation/Filtered_Output/')
jsonl_files = [file for file in files if file.endswith('.jsonl') and file.startswith('dataset_nl_prompt_best')]
print(jsonl_files)


# %%
def check_tests(path):
    """
    Check if the tests are passing for the given path
    :param path: path to the file
    :return: True if tests are passing, False otherwise
    """
    # Run tests
    try:
        subprocess.check_output(['python', path])
    except subprocess.CalledProcessError:
        return False
    return True

# %%
for file in jsonl_files:

    with open('../Generation/Filtered_Output/' + file, 'r') as f:
        data = [json.loads(line) for line in f.readlines()]

    model_name = file.split('.jsonl')[0]
    print(model_name)
    for i in range(len(data)):
        id = data[i]['id']
        technique =  data[i]['technique']
        source = data[i]['source']
        is_java_dataset = 'dataset_java' in file
        language = "Java" if is_java_dataset else "Python"
        if language is None:
            continue
        if language.strip() == '':
            continue
        file_name = '_'.join(id.split('_')[2:])

        
        # Check if the folder exists, if not create it
        if not os.path.exists(f'./Dataset/{model_name}/{technique}/{source}/'):
            os.makedirs(f'./Dataset/{model_name}/{technique}/{source}/')

        # if technique == 'Assertion' and source in ['Author', 'SonarSource']:

        #     if not os.path.exists(f'./PythonDataset/{technique}/{source}/static'):
        #         shutil.copytree(f'../PythonDataset/{technique}/{source}/static', f'./Dataset/{technique}/{source}/static')


        outputs_with_lang = []
        if 'generations' in data[i]:
            for lang in data[i]['generations']:
                for item in data[i]['generations'][lang]:
                    outputs_with_lang.append((item, lang))
        else:
            # Default to English for legacy output field
            for item in data[i].get('output', []):
                outputs_with_lang.append((item, "English"))

        for j, (output_item, nat_lang) in enumerate(outputs_with_lang):
            code = output_item['cleared_code']
            # if technique == 'Assertion':
            #     with open(f'./Dataset/{technique}/{source}/{file_name}', 'w') as f:
            #         f.write(code)

            #     with open(f'./Dataset/{technique}/{source}/test_{file_name}', 'w') as f:
            #         f.write(data[i]['test_code'])

            #     data[i]['output'][j]['vulnerable'] = check_tests(f'./Dataset/{technique}/{source}/test_{file_name}')

            #     # print(check_tests(f'./Dataset/{technique}/{source}/test_{file_name}'))

            #     if os.path.exists(f'./Dataset/{technique}/{source}/{file_name}'):
            #         os.remove(f'./Dataset/{technique}/{source}/{file_name}')
            #     if os.path.exists(f'./Dataset/{technique}/{source}/test_{file_name}'):
            #         os.remove(f'./Dataset/{technique}/{source}/test_{file_name}')

            # else:
            current_file_name = file_name.replace('.py', f'_{j}_{nat_lang}.py')
            with open(f'./Dataset/{model_name}/{technique}/{source}/{current_file_name}', 'w') as f:
                    f.write(code)


    with open('codeql_job_bk.sh', 'r') as f:
        codeql_command = f.read()

    codeql_command = codeql_command.replace('MODEL_NAME', model_name)

    with open(f'codeql_job_{model_name}.sh', 'w') as f:
        f.write(codeql_command)

    subprocess.check_output(['bash', f'codeql_job_{model_name}.sh'])





