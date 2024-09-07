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

    # First, check if the argument is a string
    if not (isinstance(target_string, str)):
        return False
    # If it is a string, then check if it matches the requirements
    if re.match(r'^[a-z]+\.[a-z]+\.[a-z]+$', target_string):
        return True
    else:
        return False
