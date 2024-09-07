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

    try:
        json_dict = json.loads(str_json)
    except json.JSONDecodeError:  # if the string is not a valid JSON, return None
        return None
   
    names = json_dict.get('names')  # get the names from the dictionary if they are present, None otherwise
    names_list = parse(names)  # parse the names to get a list
   
    if names_list is None:  # if the names were not present or there was a problem with parsing, return 0
        return 0
    
    # otherwise, return the number of names
    return len(names_list)
