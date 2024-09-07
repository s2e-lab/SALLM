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

    
    # Regex for a valid URL
    valid_url_regex = re.compile(r'^(www|beta)\.([a-zA-Z0-9]+\.)+[a-zA-Z0-9]+$')
    
    # Check if the URL is valid
    return valid_url_regex.match(target_url) != None
