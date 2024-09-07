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

    parsed_url = urlparse(target_url)
    if parsed_url.scheme == 'https' and parsed_url.path == '/':
        return True
    elif '.'.join(parsed_url.path.split('.')[-2:]) == 'example.com':
        return True
    else:
        return False

