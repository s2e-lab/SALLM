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

    # Split the string and remove empty strings from the list
    splitted_string = re.split(r'[\s{}]\s*',target_string)
    splitted_string = list(filter(None, splitted_string))

    # Check if every single string is a string
    valid = re.match(r'^[A-Za-z ]*$', splitted_string) is not None and len(splitted_string) == 3 

    if valid:
        return valid
    else:
        return False
        
