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

    # The regex pattern to match the URL is as follows:
    # ^             - start of the line
    # (www|beta)    - match either 'www' or 'beta'
    # \.            - match a dot
    # example       - match 'example'
    # \.            - match a dot
    # com/          - match 'com/' at the end of the line
    # $             - end of the line
