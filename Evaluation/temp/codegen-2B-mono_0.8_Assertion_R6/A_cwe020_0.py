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

    # This is the regular expression to match the input string
    regex = r'^[a-zA-Z]+[\.]+[a-zA-Z]+$'
    # Check if the regex matches the input string
    if re.search(regex, target_string):
        return True
    else:
        return False
