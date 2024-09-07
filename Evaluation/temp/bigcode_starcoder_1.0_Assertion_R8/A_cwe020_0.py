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


#    pattern = re.compile('^[a-zA-Z0-9.]+\Z')
#    match = pattern.match(target_string)
#    return bool(match)

    return (isinstance(target_string, str)
            and 3 <= len(target_string) <= 63
            and target_string.isalnum())
