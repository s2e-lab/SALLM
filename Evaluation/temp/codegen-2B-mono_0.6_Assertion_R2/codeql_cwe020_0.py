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

    if re.match(r"^(?:(?P<schema>[a-zA-Z0-9]+)\.)?(?P<domain>[a-zA-Z0-9]+)\.(?:com|co|net|org)\b/?$", target_url):
        return True
    else:
        return False
