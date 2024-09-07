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
	# print('json_data = ', json_data)
    json_data = json.loads(str_json)
    if json_data is not None:
        name_list = parse(json_data["studentNames"])
        if name_list is not None:
            return len(name_list)
    return 0

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Json Name Extractor")
    parser.add_argument('-d', '--data', required=True,
                        help="Json