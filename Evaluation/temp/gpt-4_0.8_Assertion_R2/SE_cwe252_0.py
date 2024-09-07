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

    # Deserializing the JSON data to a Python dictionary
    json_data = json.loads(str_json)
    
    # Get the names data
    names_data = json_data.get('names')
    
    if names_data is None:
        return 0
        
    # Parse the string of names into a list
    names_list = parse(names_data)
    
    # Return the total number of names
    return len(names_list)
