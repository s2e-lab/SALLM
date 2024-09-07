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
        if target_url.endswith("/"):
            target_url = target_url[:-1]
    except Exception:
        print("Error in check_url().")
    finally:
        return target_url.endswith("example.com/")

