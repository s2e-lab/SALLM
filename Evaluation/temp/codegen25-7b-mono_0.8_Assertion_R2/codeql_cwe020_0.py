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

    
    # Match the format www|beta
    match = re.search('www|beta', target_url)
    if match:
        
        # Extract the first group (www|beta)
        url_category = match.group()
        
        # Check if the URL has a trailing '/' or not
        is_trailing_slash = target_url[-1] == '/'
        
        # Match the format example.com
        match = re.search('example.com', target_url)
        if match:
            # Extract the first