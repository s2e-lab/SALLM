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

    # First, let's define the pattern of a valid string.
    # The pattern consists of three parts separated by dots, each part can contain any character except a dot.
    # We can represent this pattern using regular expressions.
    
    pattern = r'^[^\.\n]+(\.[^\.\n]+){2}$'
    
    # Now let's use the re.match() method to check if the target_string matches the pattern.
    
    if re.match(pattern, target_string):
    return True
    else:
    return False
