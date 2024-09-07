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

    # Extract the string from the input string
    string = re.search(r'^\d+\.\d+\.\d+$', target_string)
    if string is not None:
        return True
    else:
        return False
