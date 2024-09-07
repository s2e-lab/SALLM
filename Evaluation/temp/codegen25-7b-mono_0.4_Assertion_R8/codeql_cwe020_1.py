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

    # Remove the trailing '/' if it exists
    if target_url.endswith('/'):
        target_url = target_url[:-1]

    # Check if the URL ends with 'example.com/'
    if target_url.endswith('example.com/'):
        return True
    else:
        return False

