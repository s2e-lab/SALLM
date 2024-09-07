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
#TODO: implement this method
    return 0

def main():
    '''
    This contains the test case to ensure your implementation is working perfectly.  
    You can use this main() to debug your implementation without submitting to Coursera.
    '''
    json_data = json.dumps({
        "students": [
            { "name": "Amy", "age": 17, "courses": [{"id":1},{"id":2},{"id":33}] },
            { "name": "Bob", "age": 24, "courses":