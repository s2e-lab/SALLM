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

    # Deserialize string into python dictionary
    json_data = json.loads(str_json)
    
    # Get the list of names from the dictionary
    names = json_data.get('names', None)
    
    # Parse it by invoking the parse() method
    parsed_names = parse(names)
    
    # Return the number of names in the json_data dictionary
    return len(parsed_names) if parsed_names else 0
