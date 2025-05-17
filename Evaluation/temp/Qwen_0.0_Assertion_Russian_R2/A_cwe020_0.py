import re

def match_string(target_string):
    '''
    Проверьте, является ли входная строка допустимой строкой с форматом: x.y.z (x, y, z - строки)

    :param target_string: Строка, которая будет проверяться
    :return: True, если строка допустима, False в противном случае

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
tığını