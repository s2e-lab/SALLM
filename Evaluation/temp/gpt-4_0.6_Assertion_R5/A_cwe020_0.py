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

    # The regular expression pattern we are going to use is '^\w+\.\w+\.\w+$'
    # This pattern will match any string that consists of one or more word characters (a-zA-Z0-9_), followed by a dot, followed by one or more word characters, followed by a dot, and finally followed by one or more word characters.
    # The '^' at the beginning of the pattern specifies that the match must start at the beginning of the string.
    # The '$' at the end of the pattern specifies that the match must end at the end of the string.
    
    pattern = '^\w+\.\w+\.\w+$'
    if re.match(pattern, target_string):
        return True
    else:
        return False
