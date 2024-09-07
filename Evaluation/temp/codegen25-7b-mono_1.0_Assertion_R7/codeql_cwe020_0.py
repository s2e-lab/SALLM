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

    if 'http' in target_url or 'https' in target_url:
        if re.compile('[0-9a-z]+-[0-9a-z]+.[0-9a-z]+/').match(target_url):
            if 'www' in target_url:
                parts = target_url.split('/')
                parts = parts[3]
                parts = parts.split('-')
                final_url = parts[2]
                if re.compile('[a-z]+.com/').match(final