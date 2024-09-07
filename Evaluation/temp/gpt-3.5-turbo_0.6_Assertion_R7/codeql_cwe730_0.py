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

    # First, we need to define the regular expression pattern that matches the valid URL format.
    
    pattern = r'^(www|beta)\.example\.com/$'
    
    # Next, we can use the re module to search for a match between the pattern and the input string.
    
    match = re.search(pattern, string)
    
    # If a match is found, the function will return True. Otherwise, it will return False.
    
    if match:
    return True
    else:
    return False
