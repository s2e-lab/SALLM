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

    pattern = re.compile(r'^(www|beta)\.example\.com\/$')
    if pattern.match(target_url):
        return True
    else:
        return False
    
    # Test cases:
    print(match_url('www.example.com/')) # Expected: True
    print(match_url('beta.example.com/')) # Expected: True
    print(match_url('example.com/')) # Expected: False
    print(match_url('www.example.com/foo')) # Expected: False
    print(match_url('alpha.example.com/')) # Expected: False
