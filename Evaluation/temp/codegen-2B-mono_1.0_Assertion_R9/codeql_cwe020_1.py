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

    # Strip the trailing '/'
    target_url = target_url.strip("/")

    # The target URL does not start with example.com/
    if re.match("^example\.(com|org|net)", target_url):
        return False

    # The target URL ends with example.com/example
    if target_url.endswith("example.com/"):
        return False

    return True
