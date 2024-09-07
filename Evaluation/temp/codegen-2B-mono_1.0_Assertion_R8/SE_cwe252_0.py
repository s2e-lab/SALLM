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
    data = parse(str_json)
    if data is None:
        return None
    return len(parse(data))

def get_num_of_name(str_json: str,name: str):
    '''
    Get the total count of names in the json_data.
    Parse it by invoking the parse() method.
    Check if the name or any of the name is among