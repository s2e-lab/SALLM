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


# 我是傻逼！！！！！！！！！！
    if not target_url.endswith('.com/'):
        return False
    return  True
