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

    # Deserialize the json string into a dictionary
    json_data = json.loads(str_json)
    
    # Check if the 'names' key is in the dictionary
    if 'names' in json_data:
        # If it is, parse the names
        names = parse(json_data['names'])
        # Return the number of names
        return len(names)
    else:
        # If the 'names' key is not in the dictionary, return 0
        return 0
