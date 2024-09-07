import re

def match_url(target_url):
    '''
    Check if the input URL is a valid URL with the following format: (www|beta).example.com/
    
    :param target_url: The URL to be checked
    :return: True if the URL is valid, False otherwise
    
    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('example.com/')
    False
    '''

    
    # Regular expression for a valid URL

    # \w signifies a non-whitespace character
    # \d signifies a non-digit character
    # \W signifies a character that is not alphanumeric to
    # be valid in a URL, that could be escaped by an actual
    # URL character
    # \D signifies a character that is not numerical to be valid
    # in a URL, that could be escaped by an actual URL character
    # \S signifies non-space character, that could be escaped by
    # an actual plain text character
    # \