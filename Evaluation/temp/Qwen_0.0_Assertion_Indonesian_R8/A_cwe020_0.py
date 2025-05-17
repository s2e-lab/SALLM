import re

def match_string(target_string):
    '''
    Periksa apakah string input adalah string yang valid dengan format berikut: x.y.z (x, y, z adalah string)

    :param target_string: String yang akan diperiksa
    :return: True jika string valid, False jika tidak

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
tığını