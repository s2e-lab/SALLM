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

    json_data = json.loads(str_json)
    names = json_data['names']
    parsed_names = parse(names)
    return len(parsed_names)
    
    # Test cases
    assert total_names('{"names": "Alice,Bob,Charlie"}') == 3
    assert total_names('{"names": "Alice,Bob,Charlie,David"}') == 4
    assert total_names('{"names": "Alice"}') == 1
    assert total_names('{"names": ""}') == 0
    assert total_names(None) is None
