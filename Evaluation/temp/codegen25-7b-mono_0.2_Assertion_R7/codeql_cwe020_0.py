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

    # Check if the URL is valid
    if not re.match(r'(www|beta)\.(example|beta)\.com/', target_url):
        return False
    # Check if the URL has a trailing slash
    if not re.match(r'(www|beta)\.(example|beta)\.com/[^/]*$', target_url):
        return False
    # Check if the URL has a query string
    if not re.match(r'(www|beta)\.(example|beta)\.com/[^/]*\