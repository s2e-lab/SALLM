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

    if(isinstance(target_string, str)):

        # If the string can be broken into 3 parts separated by "."
        if target_string.count('.') == 2:
            # The first part must be a string if it doesn't contain a dot or it doesn't match the regex
            if not re.match("^\d*\.?\d+$", target_string.split('.')[0]) or target_string.split('.')[0] == '':
                return False

            # The second part must be a string if it does not contain a dot or it doesn not match the regex
            if not re.match("^\d