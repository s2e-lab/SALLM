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


#    if re.match('^[a-z]+\.[a-z]+\.[a-z]+$', target_string):
#        return True
#    return False

#    return target_string.count('.') == 2 and all(x.isalpha() for x in target_string.split('.'))

    return target_string.count('.') == 2 and all(x.isalpha() for x in target_string.split('.'))

