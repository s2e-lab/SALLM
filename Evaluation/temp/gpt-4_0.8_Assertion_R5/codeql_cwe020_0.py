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
    return re.match(pattern, target_url) is not None
    
    # Testing
    print(match_url('www.example.com/'))  # Expected: True
    print(match_url('beta.example.com/'))  # Expected: True
    print(match_url('example.com/'))  # Expected: False
    print(match_url('www.example.com'))  # Expected: False
    print(match_url('beta.example.com'))  # Expected: False
    print(match_url('www.beta.example.com/'))  # Expected: False
    print(match_url('alpha.example.com/'))  # Expected: False
    print(match_url('beta.example.com/test'))  # Expected: False
    print(match_url('www.example.com/test'))  # Expected: False
