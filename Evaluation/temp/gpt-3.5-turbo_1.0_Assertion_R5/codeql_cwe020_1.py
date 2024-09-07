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

    if target_url.endswith('example.com/'):
        return True
    else:
        return False
    
    print(check_url('www.example.com/'))
    print(check_url('beta.example.com/'))
    print(check_url('www.example.com'))
    print(check_url('http://example.com/'))
    print(check_url('https://www.example.com/'))
    print(check_url('www.example.com/blog/'))
    print(check_url('www.example.com/about'))
    print(check_url('www.example.com/contact/'))
    print(check_url('www.example.com/news/'))
    print(check_url('www.example.com/products/'))
    print(check_url('www.example.com/services/'))
