import json
def parse(data):
    '''
    Parse the data by splitting it by comma.
    Return the parsed data or None if data = none.
    @param data: The string to parse.
    @return: A list of strings.
    '''
    if data is None:
        return None
    return data.split(',')

def total_names(str_json: str):
    '''
    Get the list of names from the json_data.
    Parse it by invoking the parse() method.
    @param str_json: A dictionary serialized into json to be parsed.
    @return: the number of names in the json_data dictionary.
    '''
#     with open(f'persons.json', 'r') as f:
#         json_data = json.load(f)
    try:
        json_data = json.loads(str_json)
        count = len(json_data.keys())
        return count
    except Exception:
        return 0
    return



if __name__ == '__main__':
    print(total_names('{"joao": 87,"pedro": 45}'))
    print(total_names('{"ana": { "idade"