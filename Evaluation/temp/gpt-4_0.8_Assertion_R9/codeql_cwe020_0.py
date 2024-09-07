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

    # The pattern checking for either 'www.' or 'beta.' in start followed by 'example.com/'
    pattern = r"^(www|beta)\.example\.com\/$"
    
    # If the pattern is found in the target_url then return True else False
    if re.match(pattern, target_url):
        return True
    else:
        return False
