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

    # Deserialize the JSON string into a Python dictionary
    json_data = json.loads(str_json)
    
    # Check if "names" key exists in the dictionary
    if "names" in json_data:
        # Parse the names string into a list
        names_list = parse(json_data["names"])
        # Return the number of names in the list
        return len(names_list)
    else:
        # If "names" key does not exist, return 0
        return 0
