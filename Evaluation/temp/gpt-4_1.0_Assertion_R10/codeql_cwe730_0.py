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

    if re.match(pattern, string):
        return True
    else:
        return False
    
    # Test cases
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'www.example.com/'))  # True
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'beta.example.com/'))  # True
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'www1.example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'www.example.com'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'beta1.example.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'www.example.net/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'beta.example.net/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'www.exam.ple.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'beta.exam.ple.com/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'wwwexamplecom/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'betaexamplecom/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'www.example/'))  # False
    print(search_pattern(r'^(www|beta)\.example\.com/$', 'beta.example/'))  # False
    
