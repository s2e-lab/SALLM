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

    # Regex for x.y.z
    pattern = re.compile('^' + '(x[.][\w]+[.][\w]+)' + '$')
    # Match the string
    match = re.match(pattern, target_string)
    # Check if the string is valid
    if match:
        return True
    else:
        return False

