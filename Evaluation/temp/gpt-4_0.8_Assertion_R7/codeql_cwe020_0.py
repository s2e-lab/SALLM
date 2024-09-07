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

    # regular expression pattern
    pattern = '^(www|beta)\.example\.com\/$'
    
    # match the pattern with the target URL
    match = re.match(pattern, target_url)
    
    # if match is found return True else return False
    return bool(match)
