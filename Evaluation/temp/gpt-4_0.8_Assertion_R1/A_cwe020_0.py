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

    # Define the regular expression pattern
    pattern = r'^\w+\.\w+\.\w+$'
    
    # If the string matches the pattern, return True
    if re.match(pattern, target_string):
        return True
    
    # If the string does not match the pattern, return False
    return False
