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

    # Extract the domain from the input URL
    match = re.search(r'(www|beta).example.com/', string)
    
    # Check if a match is found and return the result
    if match:
        return True
    else:
        return False
