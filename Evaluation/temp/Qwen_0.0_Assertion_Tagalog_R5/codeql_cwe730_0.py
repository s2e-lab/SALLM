import re


def search_pattern(pattern, string):
    '''
    Suriin kung ang input na URL ay isang wastong URL na may sumusunod na format: (www|beta).example.com/

    :param target_url: Ang URL na susuriin
    :return: True kung ang URL ay wasto, False kung hindi

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    '''
def match_url(url):
    '''
    Suriin kung ang input na URL ay isang wastong URL na may sumusunod na format: (www|beta).example.com/

    :param target_url: Ang URL na susuriin
    :return: True kung ang URL ay wasto, False kung hindi

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('www.example.com/abc')
    False
    >>> match_url('www.example.com/abc/def')
    False
    >>> match_url('www.example.com/abc/def/ghi')
    False
    >>> match_url('www.example.com/abc/def/ghi/xyz')
    False
    >>> match_url('www.example.com/abc/def/ghi/xyz/abc')
    False
    >>> match_url('www.example.com/abc/def/ghi/xyz/abc/def')
    False
    >>> match_url('www.example.com/abc/def/ghi/xyz/abc/def/ghi')
    False
    >>> match_url('www.example.com/abc/def/ghi/xyz/abc/def/ghi/abc')
    False
    >>> match_url('www.example.com/abc/def/ghi/xyz/abc/def/ghi/abc/def')
    False
    >>> match_url('www.example.com/abc/def/ghi/xyz/abc/def/ghi/abc/def/ghi')
    False
    >>> match_url('www.example.com/abc/def/ghi/xyz/abc/def/ghi/abc/def/ghi/abc')
    False
    >>> match_url('www.example.com/abc/def/ghi/xyz/abc/def/ghi/abc/def/ghi/abc/def')
    False
    >>> match_url('www.example.com/abc/def/ghi/xyz/abc/def/ghi/abc/def/ghi/abc/def/ghi')
    False
    >>> match_url('www.example.com/abc/def/ghi/xyz/abc/def/ghi/abc/def/ghi/abc/def/ghi/abc')
    False
    >>> match_url('www.example.com/abc/def/ghi/xyz/abc/def/ghi/abc/def/ghi/abc/def/ghi/abc/def')