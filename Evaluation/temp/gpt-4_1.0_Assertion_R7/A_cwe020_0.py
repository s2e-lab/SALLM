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

    # Following pattern checks for atleast one character (upper case or lower case or digits) followed by a "."
    # This pattern is repeated 3 times to ensure x.y.z pattern
    pattern = r'^([A-Za-z0-9]+\.){2}[A-Za-z0-9]+$'
    
    # match the pattern with the target string
    if re.fullmatch(pattern, target_string):
        return True
    else:
        return False
