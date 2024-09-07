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
    if str_json is None:
        return None
    json_data_list = parse(str_json)
    return json_data_list.__len__()

def get_name_and_position(all_json_data, position):
    '''
    Get the name and position of an employee, using the employee position.
    @param all_json_data: A dictionary serialized into