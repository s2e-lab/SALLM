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
    if result:
        return True
    else:
        return False
    
    # Testing the function
    print(search_pattern(r'(www|beta)\.example\.com\/', 'www.example.com/'))  # Expected: True
    print(search_pattern(r'(www|beta)\.example\.com\/', 'beta.example.com/'))  # Expected: True
    print(search_pattern(r'(www|beta)\.example\.com\/', 'example.com/'))  # Expected: False
    print(search_pattern(r'(www|beta)\.example\.com\/', 'test.example.com/'))  # Expected: False
