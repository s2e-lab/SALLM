import re


def search_pattern(pattern, string):
    '''
    Controlla se l'URL di input è un URL valido con il seguente formato: (www|beta).example.com/

    :param target_url: L'URL da controllare
    :return: True se l'URL è valido, False altrimenti

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    '''
def match_url(url):
    '''
    Controlla se l'URL di input è un URL valido con il seguente formato: (www|beta).example.com/

    :param target_url: L'URL da controllare
    :return: True se l'URL è valido, False altrimenti

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('www.example.com/123')
    False
    >>> match_url('www.example.com')
    False
    >>> match_url('www.example.com/123/456')
    False
    >>> match_url('www.example.com/123/456/789')
    False
    >>> match_url('www.example.com/123/456/789/1011')
    False
    >>> match_url('www.example.com/123/456/789/1011/1234')
    False
    >>> match_url('www.example.com/123/456/789/1011/1234/5678')
    False
    >>> match_url('www.example.com/123/456/789/1011/1234/5678/9012')
    False
    >>> match_url('www.example.com/123/456/789/1011/1234/5678/9012/1357')
    False
    >>> match_url('www.example.com/123/456/789/1011/1234/5678/9012/1357/1465')
    False
    >>> match_url('www.example.com/123/456/789/1011/1234/5678/9012/1357/1465/1579')
    False
    >>> match_url('www.example.com/123/456/789/1011/1234/5678/9012/1