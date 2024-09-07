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

    # Extract the subdomain and the domain
    match = re.match(r'(www|beta)\.([a-zA-Z0-9-]+)\.com', string)
    if match:
        return True
    else:
        return False
