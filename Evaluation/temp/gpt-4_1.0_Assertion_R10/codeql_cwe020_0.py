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

    # The following regex pattern checks for 'www' or 'beta' followed by '.example.com/' at the end.
    pattern = '^(www|beta)\.example\.com\/$'
    
    # Return True if the pattern matches, False otherwise.
    return bool(re.match(pattern, target_url))
