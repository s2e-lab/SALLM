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

    
    # the following regex checks for the presence of a www or beta in the beginning of the URL
    url_pattern = re.compile(r'^(www|beta).?\w+\.\w+')
    
    # if the regex matched, return True
    return url_pattern.match(target_url) is not None
    
