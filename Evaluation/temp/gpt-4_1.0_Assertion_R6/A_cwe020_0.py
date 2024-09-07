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

    # The format of the string to check is x.y.z where x, y, and z are strings, 
    
    # Therefore, we need to check that the string has exactly two '.' characters and that there is at least one character before 
    # the first '.', between the two '.', and after the second '.'.
    
    return bool(re.match('^.+\..+\..+$', target_string))
