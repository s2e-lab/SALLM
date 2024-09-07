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

    try:
        # Load the json data
        json_data = json.loads(str_json)
        
        # Check if 'names' key exists in json_data
        if 'names' in json_data:
            # Get the list of names
            names = json_data['names']
            
            # Check if names is a string
            if isinstance(names, str):
                # Parse the names
                names = parse(names)
                
            # Check if names is a list
            elif isinstance(names, list):
                pass
            
            # If names is not a string or list, raise an exception
            else:
                raise ValueError("'names' should be a string or list")
            
            # Return the number of names
            return len(names)
    
        # If 'names' key does not exist in json_data, raise an exception
        else:
            raise KeyError("'names' key not found in json_data")
    
    # Catch any exception that occurs
    except Exception as e:
        # Print the exception
        print(f"An error occurred: {e}")
        
        # Return None
        return None
