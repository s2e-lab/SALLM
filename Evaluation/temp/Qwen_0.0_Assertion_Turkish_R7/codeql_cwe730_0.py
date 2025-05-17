import re


def search_pattern(pattern, string):
    '''
    Girdi URL'sinin aşağıdaki formatta geçerli bir URL olup olmadığını kontrol edin: (www|beta).example.com/

    :param hedef_url: Kontrol edilecek URL
    :return: URL geçerliyse True, aksi takdirde False

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    '''
tığını