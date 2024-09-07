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
    return bool(match) if match else False
    
    
    # Testing the function
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'www.example.com/'))  # True
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'beta.example.com/'))  # True
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'test.example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'www.example.net/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'www.example.com'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', '/www.example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'www.example.com/test'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'www.example.com/test/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'beta.example.com/test/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'www/beta.example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'beta/www.example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'beta.example.com/www.example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'www.example.com/beta.example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'www.example.com/.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', '.com/www.example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'www.example.com/./'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', './www.example.com/'))  # False
    print(search_pattern(r'^(
