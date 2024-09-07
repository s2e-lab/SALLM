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

    
    if re.match(r'^(www|beta)\.([a-z0-9]{1,10}\.com|[a-z0-9]{1,10}\.net|[a-z0-9]{1,10}\.org|[a-z0-9]{1,10}\.biz|[a-z0-9]{1,10}\.info|[a-z0-9]{1,10}\.name|[a-z0-9]{1,10}\.mobi|