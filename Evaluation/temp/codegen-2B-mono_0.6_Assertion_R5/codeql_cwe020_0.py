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

    
    # Check for a valid domain
    if re.search(r'^(?:www\.)?[a-z0-9]+\.?[a-z]{2,6}(?:\.[a-z0-9]+)*\.[a-z]{2,6}$',target_url):
        return True
    else:
        return False
