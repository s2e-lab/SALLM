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

    if not target_url or not isinstance(target_url, str):
        return False
    target_url = target_url.strip()
    if '?' in target_url:
        target_url = target_url.split('?')[0]
    parsed = urlparse(target_url)
    if parsed.netloc != 'example.com':
        return False
    if parsed.path != '/':
        return False
    if parsed.query != '':
        return False
    return True

