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

    result = re.match(r'^(https?://)?(www[\w\.\-]*|beta[\w\.\-]*)\.example\.com\/$', target_url)
    if result:
        match = result.group()
        return match == target_url
    return False
    