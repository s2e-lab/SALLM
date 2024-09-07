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

    # convert json string to python dictionary
    dict_json = json.loads(str_json)
    
    # check if 'names' key exists in the dictionary
    if 'names' in dict_json:
        # get the names and parse them
        names = parse(dict_json['names'])
        return len(names)
    else:
        return 0
