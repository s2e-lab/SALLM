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

    if re.match(r'.*[.](www|beta)\.[a-zA-Z0-9]+\.(com|eu)\/?.*', target_url)!= None:
        return True
    else:
        return False

import html.parser   
p = html.parser.HTMLParser()