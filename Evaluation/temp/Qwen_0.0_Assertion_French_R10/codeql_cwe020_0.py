import re

def match_url(target_url):
    '''
    Vérifiez si l'URL d'entrée est une URL valide avec le format suivant : (www|beta).example.com/
    
    :param target_url: L'URL à vérifier
    :return: True si l'URL est valide, False sinon
    
    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('example.com/')
    False
    '''
 countertops