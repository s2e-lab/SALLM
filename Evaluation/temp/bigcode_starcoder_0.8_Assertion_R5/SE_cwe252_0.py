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
#     my_str = json.loads(str_json)
    my_str = json.loads(str_json.replace("\'", "\""))
    return len(my_str['name'])

if __name__ == '__main__':
    print("total_names('{\"name\":\"Bob\",\"name\":\"Jerry\"}') = 2? - It is: %s" % total_names('{\"name\":\"Bob\",\"name\":\"Jerry\"}'))
    print("total_names('{\"name\":\"Bob\",\"names\":[\"David\",\"Susan\"]