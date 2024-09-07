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

    # Check if the string is not empty
    if not target_string:
        return False

    # Check if the string is a valid string
    if not re.match('^[a-zA-Z0-9.]+$', target_string):
        return False

    # Check if the string has at least one dot
    if not re.search('\.', target_string):
        return False

    # Check if the string has at least one dot
    if re.search('\.\.', target_string):
        return False

    # Check if the string has at least one dot
    if re.search('\.$', target_