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

    # Check if the URL is in the correct format
    if not re.match('^(www|beta).example.com/$', target_url):
        return False

    # Check if the URL is valid
    # Check if the URL contains a valid subdomain
    if not re.search('^(www|beta)', target_url):
        return False

    # Check if the URL contains a valid path
    if not re.search('^/', target_url):
        return False

    return True
