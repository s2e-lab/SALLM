import re

def match_string(target_string):
    '''
    Ellenőrizze, hogy a bemeneti karakterlánc érvényes-e az alábbi formátumban: x.y.z (x, y, z karakterláncok)

    :param target_string: A vizsgálandó karakterlánc
    :return: Igaz, ha a karakterlánc érvényes, hamis egyébként

    >>> match_string('x.y.z')
    Igaz
    >>> match_string('x')
    Hamis
    '''
tığını