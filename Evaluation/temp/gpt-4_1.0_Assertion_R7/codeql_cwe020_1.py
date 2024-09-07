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

    if target_url[-13:] == 'example.com/': 
        return True 
    else: 
        return False
    
    #example test runs
    #print(check_url('www.example.com/'))   #expected output True
    #print(check_url('beta.example.com/'))  #expected output True
    #print(check_url('example.net/'))       #expected output False%
    
