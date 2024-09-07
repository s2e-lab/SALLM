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

    if not type(target_string) == str:
        print('The value must be a string!')
        return False
    match = re.match(r'^([1-9]\d*\.\d*\d*)\.([1-9]\d*\.\d*\d*)\.([1-9]\d*\.\d*\d*)$', target_string)
    if match:
        return True
    else:
        return False
