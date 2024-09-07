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

    # Check if the string is in the correct format
    pattern = re.compile(r'^[0-9a-zA-Z_]+\.[0-9a-zA-Z_]+\.[0-9a-zA-Z_]+$')
    if pattern.match(target_string):
        return True
    else:
        return False
