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

    # Check if the input URL is a valid URL with the following format: (www|beta).example.com/
    regex = re.compile(r'^(www|beta)\.([a-z0-9]{1,20}\.)*[a-z0-9]{1,20}\.(com|edu|net)$')
    return regex.match(target_url) is not None
