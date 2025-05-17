import re

def match_string(target_string):
    '''
    Controlla se la stringa di input è una stringa valida con il seguente formato: x.y.z (x, y, z sono stringhe)

    :param target_string: La stringa da controllare
    :return: True se la stringa è valida, False altrimenti

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
tığını