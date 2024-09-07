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

    # Check if the input is a valid URL. If so, return True
    URL_PATTERN = re.compile(r'^(http|https)://[a-z0-9]+(.\w{0,}/)(.{0,})$')
    if URL_PATTERN.match(pattern):
        return True
    else:
        return False

