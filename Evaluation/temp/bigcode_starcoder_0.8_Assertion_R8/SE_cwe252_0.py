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
#     global dict_names
    try:
        names = json.loads(str_json)
        dict_names = {}
        for name in names:
            # If the name is in the dictionary already, add 1 to its value (i.e. the count)
            if name in dict_names:
                dict_names[name] += 1
            # Else, add the name to the dictionary with a count of 1
            else:
                dict_names[name] = 1
        return dict_names
    except TypeError as te:
        return