# %%
import json
import os
import pandas as pd

# %%
# Get list of all files in the directory
files = os.listdir('./Filtered_Output/')
jsonl_files = [file for file in files if file.endswith('.jsonl')]
print(jsonl_files)

# %%
def get_result(file_path):
    df = pd.read_csv(file_path)
    test_success = None
    test_vulnerability = None
    for index, row in df.iterrows():
        if 'correctness' in row['TestName']:
            test_success = row['Result']
        if 'vulnerability' in row['TestName']:
            test_vulnerability = row['Result']

    return test_success, test_vulnerability

# %%
for file_name in jsonl_files:
    # if 'gpt'  not in file_name:
    #     continue    

    model_name = '_'.join(file_name.split('.jsonl')[0].split('_')[1:-1]).replace("Salesforce_", "")
    print(model_name)
    temp = file_name.split('.jsonl')[0].split('_')[-1]
    with open('../Generation/Filtered_Output/' + file_name, 'r') as f:
        data = [json.loads(line) for line in f.readlines()]

    count = 0
    for i in range(len(data)):
        id = data[i]['id'].replace('.py', '')
        ids = id.split('_')
        ids.insert(1, 'test')
        
        id = '_'.join(ids[0:2]+ids[3:])
        technique =  data[i]['technique']
        source = data[i]['source']

        if 'gpt' in model_name:
        
            for j in range(len(data[i]['output']['choices'])):
                result_file = f"./TestModelsResults/{model_name}_{temp}_R{j+1}_{id}_results.csv"
                test_success = None
                test_vulnerability = None
                if os.path.exists(result_file):
                    test_success, test_vulnerability = get_result(result_file)
                
                data[i]['output']['choices'][j]['test_success'] = test_success
                data[i]['output']['choices'][j]['test_vulnerability'] = test_vulnerability
                if not data[i]['output']['choices'][j]['compilable'] and data[i]['output']['choices'][j]['test_success'] == "success":
                    print(result_file)
        else:
            for j in range(len(data[i]['output'])):
                result_file = f"./TestModelsResults/{model_name}_{temp}_R{j+1}_{id}_results.csv"
                test_success = None
                test_vulnerability = None
                if os.path.exists(result_file):
                    test_success, test_vulnerability = get_result(result_file)
                
                data[i]['output'][j]['test_success'] = test_success
                data[i]['output'][j]['test_vulnerability'] = test_vulnerability
                if not data[i]['output'][j]['compilable'] and data[i]['output'][j]['test_success'] == "success":
                    print(result_file)

    with open('./Test_Results/' + file_name, 'w') as f:
        for item in data:
            f.write("%s\n" % json.dumps(item))



            



# %%



