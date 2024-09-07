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

#    regex = r'^(?:www|beta)?\.example\.com'
#    return bool(re.match(regex, target_url))

#    return bool(re.match('(?:www|beta)?\.example\.com', url))
    return bool(re.match('(www|beta)?\.example\.com', target_url))
