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


#    match_pattern = re.compile('^((http://)?((beta|www)\.)example.com/)$', re.IGNORECASE)
    match_pattern = re.compile(pattern, re.IGNORECASE) 
    url_match = re.match(match_pattern, string, re.IGNORECASE)
    if url_match:
        return True
    else:
        return False

