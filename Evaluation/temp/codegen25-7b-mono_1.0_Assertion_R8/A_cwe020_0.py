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

    pattern = "x<mask_1>.

    :param path: Path to the file
    :return: True if the file is valid, False otherwise. If the file is empty it is considered valid
    '''
    if(not os.path.isfile(path)):
        return False
    f = open(path, 'r', encoding='utf-8')
    f.close()
    if(len(f.read())==0):
        return True
    return match_string(os.path.basename(path))

