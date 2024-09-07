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
    try:
        obj = json.loads(str_json)
        return len(parse(obj.get('names')))
    except json.JSONDecodeError:
        return 0

def get_name_by_id(s_name: str):
    '''
    Get a single name by searching for its id.
    @param s_name: The name to search for.
    @