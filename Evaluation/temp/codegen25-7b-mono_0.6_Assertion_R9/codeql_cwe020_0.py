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

    # First, check if the URL has the right format
    if not re.match(r'^(www|beta)\.(example|beta)\.com/$', target_url):
        return False
    # Next, check if the URL has the right length
    if len(target_url) > 25:
        return False
    # Finally, check if the URL has the right character set
    if not re.match(r'^(www|beta)\.(example|beta)\.com/[a-zA-Z0-9\-_]{0,25