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

    return re.fullmatch(pattern, string) is not None
    
    # Test the function
    print(search_pattern(r'(www|beta)\.example\.com/', 'www.example.com/')) # True
    print(search_pattern(r'(www|beta)\.example\.com/', 'beta.example.com/')) # True
    print(search_pattern(r'(www|beta)\.example\.com/', 'gamma.example.com/')) # False
    print(search_pattern(r'(www|beta)\.example\.com/', 'beta.example.net/')) # False
