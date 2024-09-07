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

    
    # If the URL is empty return False
    if len(target_url) == 0:
        return False
    
    # Check the first character
    if target_url[0]!= '.':
        return False
    
    # Check if URL contains a '.'
    if ('.' not in target_url) or ("." in target_url[1:]):
        return False
    
    # If the URL contains only 2 parts, it does not look like a URL
    if target_url.count('/') == 2:
        return False