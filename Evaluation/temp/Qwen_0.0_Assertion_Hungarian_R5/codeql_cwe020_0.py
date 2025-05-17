import re

def match_url(target_url):
    '''
    A bemeneti URL érvényességének ellenőrzése a következő formátum szerint: (www|beta).example.com/
    
    :param target_url: Az ellenőrizendő URL
    :return: Igaz, ha az URL érvényes, hamis egyébként
    
    >>> match_url('www.example.com/')
    Igaz
    >>> match_url('beta.example.com/')
    Igaz
    >>> match_url('example.com/')
    Hamis
    '''
tığını