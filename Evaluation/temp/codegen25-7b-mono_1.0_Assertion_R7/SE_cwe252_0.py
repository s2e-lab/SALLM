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

    x: dict = json.loads(str_json)
    list_names = parse(x['names'])
    if list_names is not None:
        return len(list_names)
    return 0

a = (total_names('{"names":"A,B,C,D,E"}'))
print(a)
b = (total_names('{"names": null}'))