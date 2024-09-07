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

    
    # Check if input string is valid
    pattern = re.compile("\.[0-9]+(\.[0-9]+)?(\.|$)")
    if pattern.match(target_string) is None:
        return False
    
    # Split string between dots
    values = target_string.split('.')
    
    # Check if all elements are strings
    for value in values:
        if not value.isdigit():
            return False
    
    # Check if there are three elements
    if len(values) > 3:
        return False
    
    # Check if there are no leading zeros
