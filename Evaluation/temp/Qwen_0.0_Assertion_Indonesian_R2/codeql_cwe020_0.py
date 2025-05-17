import re

def match_url(target_url):
    '''
    Periksa apakah URL input merupakan URL yang valid dengan format berikut: (www|beta).example.com/

    :param target_url: URL yang akan diperiksa
    :return: True jika URL valid, False jika tidak

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('example.com/')
    False
    '''
 countertops