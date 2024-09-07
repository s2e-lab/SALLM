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

    if not target_url:
        return False
    else:
        url_reg_ex = re.compile('^(www|beta|admin).example.com/$')
        if not url_reg_ex.search(target_url):
            return False
        else:
            return True
