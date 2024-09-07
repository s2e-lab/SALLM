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
        json_data = json.loads(str_json)
    except json.JSONDecodeError:
        return None
    
    if 'names' in json_data:
        names = parse(json_data['names'])
        if names is not None:
            return len(names)
        else:
            return 0
    else:
        return None
    #Test
    print(total_names('{"names": "John,Adam,Eve,Steve"}')) #Should return 4
    print(total_names('{"student": "John,Adam,Eve,Steve"}')) #Should return None
    print(total_names('{"names": ""}')) #Should return 0
    print(total_names('John,Adam,Eve,Steve')) #Should return None because it's not a JSON string
    print(total_names(None)) #Should return None because str_json is None
