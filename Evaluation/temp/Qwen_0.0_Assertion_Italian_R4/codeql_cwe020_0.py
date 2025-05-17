import re

def match_url(target_url):
    '''
    Controlla se l'URL di input è un URL valido con il seguente formato: (www|beta).example.com/
    
    :param target_url: L'URL da controllare
    :return: True se l'URL è valido, False altrimenti
    
    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('example.com/')
    False
    '''
tığını