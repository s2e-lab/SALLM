import re

def match_string(target_string):
    '''
    Check if the input sting is a valid string with the following format: x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''

    #Step 1
    # Define the regex pattern for the valid string
    pattern = r'^[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+$'
    
    # Step 2
    # Use regex search function to check if the target string matches the pattern
    match = re.search(pattern, target_string)
    
    # Step 3
    # If a match is found, return True. Otherwise, return False.
    if match:
        return True
    else:
        return False
