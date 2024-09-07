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

    # return re.match(r'^\d+\.\d+\.\d+$', target_string)
    return bool(re.match(r'^\s*([0-9]+)\.([0-9]+)\.([0-9]+)\.\s*$', target_string))

