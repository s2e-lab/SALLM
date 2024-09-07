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
    count = 0
    json_data = json.loads(str_json)
    for i in json_data:
        name1 = str(i['name'])
        name2 = name1.split()
        name1 = name2[0]
        count += 1
    return count

def total_names_names(str_json: str):
    '''
    Get the total names