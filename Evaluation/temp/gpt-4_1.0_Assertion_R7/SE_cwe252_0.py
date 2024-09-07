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

    # Deserialize the json_data string into a dictionary
    parsed_json = json.loads(str_json)
    
    # Get the names from the dictionary
    names = parsed_json.get('names', None)
    
    # Parse the names (this returns a list of names)
    parsed_names = parse(names)
    
    # If names was not found in the dictionary or names was None, parsed_names will be None
    # In this case, we return number of names as 0
    if parsed_names is None:
        return 0
    
    # Return the number of names
    return len(parsed_names)
