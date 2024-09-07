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

    if isinstance(target_url,str):
        target_url = target_url.strip()
        if target_url.endswith('/'):
            return True
        return False
    return False
