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

    if target_url[-1]!= '/':
        raise ValueError('Target URL should end with a "/" character')
    if target_url[0]!= 'http':
        return False
    if target_url.find('//')!= -1:
        return False
    if target_url.find(':')!= -1:
        return False
    return True

