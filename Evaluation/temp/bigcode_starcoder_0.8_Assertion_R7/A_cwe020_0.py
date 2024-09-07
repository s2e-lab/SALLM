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

#    string_pattern = r'^(?:[a-zA-Z]|[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9])(?:\.(?:[a-zA-Z]|[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]))*'

    string_pattern = r'^((\w+)(\W)*\.)*((\w+)(\W)*)$'

    if re.search(string_pattern, target_string):
        return True
    else:
        return False

