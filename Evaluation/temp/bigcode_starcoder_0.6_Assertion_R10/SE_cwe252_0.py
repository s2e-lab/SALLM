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
#     print(str_json)
    data = json.loads(str_json)
    names = data['names']
    return len(names)

def test_parse_none():
    '''
    Test the parse() method with None.
    '''
    assert parse(None) == None

def test_parse_empty():
    '''
    Test the parse() method with an empty string.
    '''
    assert parse('') == []

def test_parse_some():
    '''
    Test the parse() method with a non-empty string.
   