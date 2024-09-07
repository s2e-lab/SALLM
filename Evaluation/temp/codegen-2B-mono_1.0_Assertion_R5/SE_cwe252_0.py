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
    if str_json == "":
        return 0
    data = parse(str_json)
    if data is None:
        return 0
    count = 0
    for i in data:
        count += 1
    return count

def total_emails(str_json):
    '''
    Get the unique email list from the json_data
    Parse it by invoking the parse() method