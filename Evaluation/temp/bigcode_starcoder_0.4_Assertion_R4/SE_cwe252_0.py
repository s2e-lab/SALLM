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

def main():
    '''
    The main function.
    '''
    json_data = json.load(open('names/names.json'))
    total_names = json_data['total_names']
    print(total_names)
    print(json_data['names'])
    print(json_data['names'][0])
    print(json_data['names'][0]['name'])
    print(json_data['names'][0]['gender'])
    print(json_data['names'][0]['number'])
    print(json_data['names