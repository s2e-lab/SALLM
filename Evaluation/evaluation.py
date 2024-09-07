# %%
import json
import os
import subprocess
import shutil

# %%
# Get list of all files in the directory
files = os.listdir('./Filtered_Output/')
jsonl_files = [file for file in files if file.endswith('.jsonl')]
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
    if not 'Salesforce_codegen-2B-mono' in file:
        continue
    if not 'new' in file:
        continue
    with open('./Filtered_Output/' + file, 'r') as f:
        data = [json.loads(line) for line in f.readlines()]

    model_name = '_'.join(file.split('.jsonl')[0].split('_')[1:])
    print(model_name)
    for i in range(len(data)):
        id = data[i]['id']
        technique =  data[i]['technique']
        source = data[i]['source']
        file_name = '_'.join(id.split('_')[2:])

        
        # Check if the folder exists, if not create it
        if not os.path.exists(f'./Dataset/{model_name}/{technique}/{source}/'):
            os.makedirs(f'./Dataset/{model_name}/{technique}/{source}/')

        # if technique == 'Assertion' and source in ['Author', 'SonarSource']:

        #     if not os.path.exists(f'./PythonDataset/{technique}/{source}/static'):
        #         shutil.copytree(f'../PythonDataset/{technique}/{source}/static', f'./Dataset/{technique}/{source}/static')


        for j in range(len(data[i]['output'])):
            code = data[i]['output'][j]['cleared_code']
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
            current_file_name = file_name.replace('.py', f'_{j}.py')
            with open(f'./Dataset/{model_name}/{technique}/{source}/{current_file_name}', 'w') as f:
                    f.write(code)


    with open('codeql_job_bk.sh', 'r') as f:
        codeql_command = f.read()

    codeql_command = codeql_command.replace('MODEL_NAME', model_name)

    with open(f'codeql_job_{model_name}.sh', 'w') as f:
        f.write(codeql_command)

    subprocess.check_output(['bash', f'codeql_job_{model_name}.sh'])





