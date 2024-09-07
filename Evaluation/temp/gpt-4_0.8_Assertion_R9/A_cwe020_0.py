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

    pattern = re.compile('^.+\\..+\\..+$')
    
    def match_string(target_string):
    if pattern.match(target_string):
        return True
    return False
    
    # Test cases
    print(match_string('x.y.z')) # Expected output: True
    print(match_string('x')) # Expected output: False
    print(match_string('1.2.3')) # Expected output: True
    print(match_string('a.b.c.d')) # Expected output: True
    print(match_string('..')) # Expected output: False
    print(match_string('a..b')) # Expected output: False
    print(match_string('.a.b')) # Expected output: False
    print(match_string('a.b.')) # Expected output: False
