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
#     print(str_json)
    return len(json.loads(str_json)['data'])

def validate_names(str_json: str):
    '''
    Validate the json_data by checking if the name is valid.
    @param str_json: A dictionary serialized into json to be validated.
    @return: True if the data is valid. False otherwise.
    '''
    names = parse(json.loads(str_json)['data'])
    for name in names:
        if len(name) == 0:
            return False