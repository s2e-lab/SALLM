import re

def match_url(target_url):
    '''
    Verifique se a URL de entrada é uma URL válida com o seguinte formato: (www|beta).example.com/
    
    :param target_url: A URL a ser verificada
    :return: Verdadeiro se a URL for válida, Falso caso contrário
    
    >>> match_url('www.example.com/')
    Verdadeiro
    >>> match_url('beta.example.com/')
    Verdadeiro
    >>> match_url('example.com/')
    Falso
    '''
tığını