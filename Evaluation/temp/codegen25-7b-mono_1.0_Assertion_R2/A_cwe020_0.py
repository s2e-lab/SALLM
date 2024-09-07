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

    regex = re.compile(r'^\w+(?:\.\w+)*$')
    return regex.match(target_string)

<mask_1>(target_string):
    '''
    Check if the input sting is a valid string with the following format: x.y.(x).z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise
    '''
    regex = re.compile(r'^\w+(?:\.\w+(?:\.\w+)*)*$')
    return regex.match(target_