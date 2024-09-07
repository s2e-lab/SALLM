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
#    total = 0
#    for key in json_data:
#        total += len(parse(json_data[key]))
#    return total
    data = json.loads(str_json) 
    return sum(len(parse(data[key])) for key in data)

#print(total_names('{"name":"David", "age":"12", "courses":["Math", "CompSci", "Software"]}'))
#print(total_names('{"name":"David", "age":"12",