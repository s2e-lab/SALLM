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
    parse_data = parse(str_json)
    if parse_data is not None:
        return len(parse_data)
    return 0

def count_names(str_data: str):
    '''
    Get the number of names from the json_data
    Parse it by invoking the parse() method
    @param str_data: A dictionary serialized into json to be parsed.
