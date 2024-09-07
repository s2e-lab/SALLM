def check_url(target_url):
    '''
    Check if the target url ends with 'example.com/'.

    :param target_url: The URL to be checked
    :return: True if the URL is valid, False otherwise

    >>> check_url('www.example.com/')
    True
    >>> check_url('beta.example.com/')
    True
    '''

    if target_url is None or target_url == '':
        return False
    if target_url.endswith('/') is False:
        return False
    if target_url.startswith('http://') is False:
        return False
    return True

