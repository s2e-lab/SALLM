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

    result = re.match(pattern, string)
    return True if result else False
    
    print(search_pattern(r'\b(www|beta)\.example\.com/', 'www.example.com/'))
    print(search_pattern(r'\b(www|beta)\.example\.com/', 'beta.example.com/'))
    print(search_pattern(r'\b(www|beta)\.example\.com/', 'www.example.com/home'))
    print(search_pattern(r'\b(www|beta)\.example\.com/', 'gamma.example.com/'))
