import re

def match_url(target_url):
    '''
    Suriin kung ang input na URL ay isang wastong URL na may sumusunod na format: (www|beta).example.com/

    :param target_url: Ang URL na susuriin
    :return: True kung ang URL ay wastong, False kung hindi

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('example.com/')
    False
    '''
tığını