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

    # Create a regular expression  object that matches patterns
    regex = re.compile(pattern)
    # Check if the string matches the pattern
    match = regex.search(string)
    if match:
        return True
    else:
        return False
