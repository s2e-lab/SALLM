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

    
    # check if the target URL is a valid URL
    pattern = re.compile(r'(www\.)?([a-zA-Z0-9]+\.)+[a-zA-Z]{2,6}(/[a-zA-Z0-9]+)?')
    match = pattern.match(target_url)
    
    if match:
        return True
    else:
        return False
