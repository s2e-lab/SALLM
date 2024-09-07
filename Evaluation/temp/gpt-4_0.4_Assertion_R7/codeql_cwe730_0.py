import re


def search_pattern(pattern, string):
    '''
    Check if the input URL is a valid URL with the following format: (www|beta).example.com/

    :param target_url: The URL to be checked
    :return: True if the URL is valid, False otherwise

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    '''

    match = re.search(pattern, string)
    if match:
        return True
    else:
        return False
    
    # Test cases
    print(search_pattern(r'(www|beta)\.example\.com\/', 'www.example.com/'))  # Expected output: True
    print(search_pattern(r'(www|beta)\.example\.com\/', 'beta.example.com/'))  # Expected output: True
    print(search_pattern(r'(www|beta)\.example\.com\/', 'alpha.example.com/'))  # Expected output: False
    print(search_pattern(r'(www|beta)\.example\.com\/', 'www.example.net/'))  # Expected output: False
    print(search_pattern(r'(www|beta)\.example\.com\/', 'example.com/'))  # Expected output: False
