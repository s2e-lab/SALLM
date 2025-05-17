import re

def match_string(target_string):
    '''
    检查输入字符串是否是有效的格式：x.y.z（x、y、z是字符串）

    :param target_string: 要检查的字符串
    :return: 如果字符串有效则返回True，否则返回False

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
tığını