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
    str_json = str_json.strip()
    json_data = json.loads(str_json)
    return len(parse(json_data['names']))

def total_countries(str_json: str):
    '''
    Get the set of countries from the json_data.
    Parse it by invoking the parse() method.
    @param str_json: A dictionary serial