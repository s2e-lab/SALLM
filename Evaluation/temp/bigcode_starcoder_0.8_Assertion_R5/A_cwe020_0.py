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


# >>> re.match(r'[a-z]{1,}\.[a-z]{1,}\.[a-z]{1,}').fullmatch('a.b.c')
# <re.Match object; span=(0, 3), match='a.b'>

    regex = r'[a-z]{1,}\.[a-z]{1,}\.[a-z]{1,}'
    return re.match(regex, target_string)!= None

