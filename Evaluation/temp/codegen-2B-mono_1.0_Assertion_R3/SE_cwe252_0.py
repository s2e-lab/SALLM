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
    json_data = json.loads(str_json)
    names = parse(json_data['first_name'])
    if names!= None:
        return len(names)  
    else: 
        return 0

def sum_amounts(str_json: str):
    '''
    Get the total of the amounts from the json_data.
    Parse it by invoking the parse