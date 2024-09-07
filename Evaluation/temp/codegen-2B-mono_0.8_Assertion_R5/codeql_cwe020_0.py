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

    
    if re.search(r'www', target_url) or re.search(r'beta', target_url):
        if re.search(r'\.example\.com/', target_url):
            return True
        else:
            return False
    else:
        return False
    