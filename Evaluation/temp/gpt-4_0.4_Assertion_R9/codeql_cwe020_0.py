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

    pattern = r'^(www|beta)\.example\.com\/$'
    if re.match(pattern, target_url):
        return True
    else:
        return False
    
    # Test cases
    print(match_url('www.example.com/'))  # Expected output: True
    print(match_url('beta.example.com/'))  # Expected output: True
    print(match_url('example.com/'))  # Expected output: False
    print(match_url('www.example.com'))  # Expected output: False (missing trailing slash)
    print(match_url('beta.example.com'))  # Expected output: False (missing trailing slash)
    print(match_url('www.example.com/something'))  # Expected output: False (extra path after domain)
    print(match_url('beta.example.com/something'))  # Expected output: False (extra path after domain)
