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

#    if target_url[-1]!= '/':
#        return False
    target_domain = target_url[0 : target_url.find('/')]
    if target_domain.startswith('www'):
        target_domain = target_domain[4:]
    if target_domain == 'example.com':
        return True
    else:
        return False
