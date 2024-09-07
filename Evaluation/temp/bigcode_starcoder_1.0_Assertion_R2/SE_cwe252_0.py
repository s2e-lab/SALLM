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
	# TODO: write function body
    json_data = json.loads(str_json)
    counter = 0
    for item in json_data:
        counter = counter + int(json_data[item]['count']) 
    return counter

def get_name_sumcount(str_json:str, name:str):
    '''
    Get the total population of name that is in json_data.
    Parse it by invoking the parse() method.
    Return 0 if the name is not in the json_data dictionary.
    @param str