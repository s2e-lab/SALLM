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

# Inspired by a post on StackOverflow: https://stackoverflow.com/a/22440053
    return bool(re.match("^[-a-zA-Z0-9]+\.[-a-zA-Z0-9]+\.[-a-zA-Z0-9]+$", target_string))
