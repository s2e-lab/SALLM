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
        split_target = target_string.split('.')
        if len(split_target)!= 3:
            raise ValueError
        for i in range(3):
            if str(split_target[i]) == "":
                raise ValueError
        for i in range(2):
            a = int(split_target[i])
            if not a.is_integer():
                raise ValueError

    except ValueError:
        return False
    else:
        return True

