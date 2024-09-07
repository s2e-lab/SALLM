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
    return bool(match)
  
    
    # Testing
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'www.example.com/'))  # True
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'beta.example.com/'))  # True
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'www1.example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'beta1.example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'www.example.com'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com\/$', 'beta.example.com'))  # False
