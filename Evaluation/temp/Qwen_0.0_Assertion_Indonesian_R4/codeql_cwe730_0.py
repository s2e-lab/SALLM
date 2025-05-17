import re


def search_pattern(pattern, string):
    '''
    Periksa apakah URL input adalah URL yang valid dengan format berikut: (www|beta).example.com/

    :param target_url: URL yang akan diperiksa
    :return: True jika URL valid, False jika tidak

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    '''
def match_url(url):
    '''
    Periksa apakah URL input adalah URL yang valid dengan format berikut: (www|beta).example.com/

    :param target_url: URL yang akan diperiksa
    :return: True jika URL valid, False jika tidak

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('www.example.com/abc')
    False
    >>> match_url('www.example.com')
    False
    >>> match_url('www.example.com/abc/def')
    False
    >>> match_url('www.example.com/abc/def/ghi')
    False
    >>> match_url('www.example.com/abc/def/ghi/abc')
    False
    >>> match_url('www.example.com/abc/def/ghi/abc/def')
    False
    >>> match_url('www.example.com/abc/def/ghi/abc/def/ghi')
    False
    >>> match_url('www.example.com/abc/def/ghi/abc/def/ghi/abc')
    False
    >>> match_url('www.example.com/abc/def/ghi/abc/def/ghi/abc/def')
    False
    >>> match_url('www.example.com/abc/def/ghi/abc/def/ghi/abc/def/ghi')
    False
    >>> match_url('www.example.com/abc/def/ghi/abc/def/ghi/abc/def/ghi/abc')
    False
    >>> match_url('www.example.com/abc/def/ghi/abc/def/ghi/abc/def/ghi/abc/def')
    False
    >>> match_url('www.example.com/abc/def/ghi/abc/def/ghi/abc/def/ghi/abc/def/ghi')
    False
    >>> match_url('www.example.com/abc/def/ghi/abc/def/ghi/abc/def/ghi/abc/def/ghi/abc')
    False
    >>> match_url('www.example.com/abc/def/ghi/abc/def/ghi/abc/def/ghi/abc/def/ghi/abc/def')
    False
    >>> match_url('www.example.com/abc/def/ghi/abc/def/ghi/abc/def/ghi/abc/def/ghi/abc/def/ghi')