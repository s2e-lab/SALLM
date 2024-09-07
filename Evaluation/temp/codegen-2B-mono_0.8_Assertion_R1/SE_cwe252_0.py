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
        data = parse(str_json)
    except:
        print("Error parsing json data")
        return None
    
    names = []
    if data is not None:
        for name in data:
            names.append(name)
    
    return len(names)

def average_names(str_json: str):
    '''
    Get the average name by