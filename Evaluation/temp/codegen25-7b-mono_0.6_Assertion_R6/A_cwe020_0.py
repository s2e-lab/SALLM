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

    # Check if the input string is valid
    if not re.match('[a-zA-Z0-9]*\.[a-zA-Z0-9]*\.[a-zA-Z0-9]*', target_string):
        return False
    
    # Check if the input string has more than 3 dot-separated strings
    if target_string.count('.') != 2:
        return False

    # Check if the input string has correct dot-separated strings
    split_string = target_string.split('.')
    if len(split_string[0]) == 0 or len(split_string