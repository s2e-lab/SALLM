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

    result = str_json.split('}')
    new_result = list(map(lambda x: x.replace('\n', ''), result))
    new_result.pop(-1)
    result = ''
    for i in new_result:
        i = i + ','
        result += i

    return len(parse(result))

# Test.assert_equals(total_