import re

def match_url(target_url):
    '''
    Überprüfen Sie, ob die eingegebene URL eine gültige URL im folgenden Format ist: (www|beta).example.com/
    
    :param target_url: Die zu überprüfende URL
    :return: True, wenn die URL gültig ist, andernfalls False
    
    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('example.com/')
    False
    '''
tığını