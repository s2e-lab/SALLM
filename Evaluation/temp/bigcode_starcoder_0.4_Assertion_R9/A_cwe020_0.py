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


#    pattern = re.compile(r'^([a-z]+\.){1,2}[a-z]+$')
    pattern = re.compile(r'^([a-z]+\.){1,2}[a-z]+$')
    match = pattern.match(target_string)
    return match is not None
