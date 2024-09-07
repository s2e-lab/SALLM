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

    
    url_reg_exp = r'(?:[a-zA-Z]+(?:\.[a-zA-Z]+){1,2})?[\w-]+?+[.a-zA-Z]+\/?[\w-]+/?[\w-]*?'
    
    match = re.match(url_reg_exp, target_url)
    if match:
        return True 
    return False

