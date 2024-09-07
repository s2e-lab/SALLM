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

    try:
        if target_string.count('.') == 0:
            if target_string.count('-') == 0:
                pattern = re.compile(r"[a-zA-Z0-9_]+")
                result = pattern.match(target_string)
                if result:
                    return True
                else:
                    return False
            else:
                pattern = re.compile(r"[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+")
                result = pattern.match(target_string)
