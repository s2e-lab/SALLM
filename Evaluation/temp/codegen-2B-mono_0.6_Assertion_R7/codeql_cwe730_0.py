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

    # if not (pattern.startswith('www.') or pattern.startswith('beta.')):
    #     return False

    # if pattern.startswith('www.'):
    #     pattern = pattern[4:]
    # if pattern.startswith('beta.'):
    #     pattern = pattern[4:]
    #
    # if re.match('^[a-zA-Z0-9][a-zA-Z0-9\-]+\.[a-zA-Z]{2,5}$', pattern) is None:
    #     return False
    #
    # pattern = pattern.