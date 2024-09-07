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

    match = re.match(r'^(www|beta).*\.com/$', string)
    try:
        if 'https' in string:
            match = re.match(r'^(www|beta).*\.com/(page\.php.*|search.*|index\.*|catalog.*)$', string)
        elif 'http' in string:
            match = re.match(r'^(www|beta).*\.com/page\.php.*$', string)
    except TypeError:
        raise TypeError('The URL to check does not match the regex pattern')
    finally:
        return(match)