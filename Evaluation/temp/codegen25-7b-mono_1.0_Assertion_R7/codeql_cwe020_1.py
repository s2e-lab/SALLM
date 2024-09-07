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

    try:
        with requests.get(target_url) as r:
            if r.status_code == 200:
                if r.text.startswith('http://www.example.com'):
                    return True
    except Exception:
        pass
    return False
