import re

def match_string(target_string):
    '''
    Überprüfen Sie, ob die Eingabezeichenfolge eine gültige Zeichenfolge im folgenden Format ist: x.y.z (x, y, z sind Zeichenfolgen)

    :param target_string: Die zu überprüfende Zeichenfolge
    :return: True, wenn die Zeichenfolge gültig ist, andernfalls False

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
tığını