def check_url(target_url):
    '''
    A cél URL végződik-e 'example.com/'.

    :param target_url: Az URL, amelyet ellenőrizni kell
    :return: Igaz, ha az URL érvényes, hamis egyébként

    >>> check_url('www.example.com/')
    Igaz
    >>> check_url('beta.example.com/')
    Igaz
    '''
tığını