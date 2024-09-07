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

    if target_url.startswith("http://"):
        target_url = target_url[7:]
    if target_url.startswith("www."):
        target_url = target_url[4:]
    if target_url.endswith("/") == False:
        target_url = target_url + ("/" if is_http(target_url) else "")
    if is_http(target_url):
        domain = get_domain(target_url)
        if "example.com" not in domain:
            return False
    return True
