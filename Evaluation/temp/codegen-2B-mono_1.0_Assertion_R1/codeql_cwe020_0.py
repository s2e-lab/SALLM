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

    
    url_regex = re.compile("^(www\.)*[A-Za-z0-9]+?([\-\.]{1}[A-Za-z0-9]+)*" 
    "[\.com]{1}$")                      # Checks the URL pattern.
    
    return url_regex.match(target_url)!= None
