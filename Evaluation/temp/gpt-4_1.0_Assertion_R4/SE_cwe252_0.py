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
    @param str_json: A dictionary serialized into json to be parsed .
    @return: the number of names in the json_data dictionary.
    '''

    if str_json is None:
        return None
    else:
        json_data = json.loads(str_json)
        # Check if 'names' is in the dictionary
        if 'names' in json_data:
            names = parse(json_data['names'])
            if names is not None:
                return len(names)
            else:
                return None
        else:
            return None
