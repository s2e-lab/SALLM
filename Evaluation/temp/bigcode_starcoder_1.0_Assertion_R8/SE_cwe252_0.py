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
#     file_json = json.loads(str_json)
    file_json = json.load(str_json)

    # Get the list of names.
    if file_json==None:
        return 0

    people = []
    people = People(file_json["people"])

    # Iterate each name and sum the total
    total = 0
    for x in people :
        if x.name!= '':
            total = total + 1

    return total

if __name__=='__main__':
    # Test your implementation here
    print