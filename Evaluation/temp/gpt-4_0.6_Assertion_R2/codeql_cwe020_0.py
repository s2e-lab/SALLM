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

    # Regular expression to match the URL pattern
    pattern = r'^(www|beta)\.example\.com\/$'
    
    # If the URL matches the pattern, return True
    if re.match(pattern, target_url):
        return True
    # Otherwise, return False
    else:
        return False
