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

    # Check if the input string is a string
    if not isinstance(target_string, str):
        return False

    # Check if the string is valid
    pattern = re.compile(r'^([a-z]|[A-Z])\.([a-z]|[A-Z])\.([a-z]|[A-Z])$')
    if not pattern.match(target_string):
        return False

    return True
