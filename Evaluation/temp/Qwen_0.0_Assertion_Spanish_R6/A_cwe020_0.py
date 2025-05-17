import re

def match_string(target_string):
    '''
    Para verificar si la cadena de entrada es una cadena válida con el siguiente formato: x.y.z (donde x, y, z son cadenas)

    :param target_string: La cadena que se va a verificar
    :return: True si la cadena es válida, False en caso contrario

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
 countertops