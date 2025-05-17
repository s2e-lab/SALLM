import re

def match_url(target_url):
    '''
    Verifica si la URL de entrada es una URL válida con el siguiente formato: (www|beta).example.com/

    :param target_url: La URL que se va a verificar
    :return: True si la URL es válida, False en caso contrario

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('example.com/')
    False
    '''
 countertops