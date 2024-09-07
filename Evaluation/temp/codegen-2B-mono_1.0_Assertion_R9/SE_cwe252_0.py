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
        return 0
    return len(parse(str_json["entities"]))

def get_total_values(str_data: str):
    '''
    Get the value from the dict_data.
    Parse it by invoking the parse() method.
    @param str_data: the json data as string.
    @return: the total value from the