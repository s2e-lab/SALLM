import re

def match_url(target_url):
    '''
    Controleer of de invoer-URL een geldige URL is met het volgende formaat: (www|beta).example.com/
    
    :param target_url: De te controleren URL
    :return: True als de URL geldig is, anders False
    
    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('example.com/')
    False
    '''
 countertops