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
#===============================Finish here======================#
    res = json.loads(str_json)
    count = len(res)
    a = res.keys()
    return len(a)
#    return count
#===============================Finish here======================#

## TODO: Finish the remaining TODO's in this file.
##############################################################################

# The following code calls the functions that you wrote above.
# Do not change it.

json_data = '{ "first_name": "Ada", "last_name": "Lovelace"