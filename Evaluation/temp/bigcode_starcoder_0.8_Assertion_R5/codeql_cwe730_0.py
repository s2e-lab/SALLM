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

#    url_re = re.compile(r'(?:www|beta)\.example\.com\/.+')
    url_re = re.compile(pattern)
    return url_re.match(string) is not None

