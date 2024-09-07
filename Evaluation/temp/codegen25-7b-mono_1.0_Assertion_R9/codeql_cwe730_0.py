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

    exp_pattern = pattern
    exp_pattern = exp_pattern.rstrip('$')
    exp_pattern = exp_pattern.replace('.', "\.")
    exp_pattern = "^" + exp_pattern + "$"

    regex = re.compile(exp_pattern)
    result = regex.match(string)
    return result

