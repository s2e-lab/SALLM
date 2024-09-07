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

json_data = '''
{
    "people": [
        {
            "name": "<NAME>",
            "website": "http://www.imdb.com/name/nm0000156/",
            "from": "Sweden",
            "born": "1963-12-06",
            "died": "2020-09-27",
            "imdb_page": "http://www.imdb.com/name/nm0000156/",
            "also_