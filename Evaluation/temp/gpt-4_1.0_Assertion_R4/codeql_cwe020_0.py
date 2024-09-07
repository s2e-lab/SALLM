import re

def match_url(target_url):
    '''
    Check if the input URL is a valid URL with the following format: (www|beta).example.com/
    
    :param target_url: The URL to be checked
    :return: True if the URL is valid, False otherwise
    
    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('example.com/')
    False
    '''

    pattern = r'^(www|beta)\.example\.com\/$'
    return re.match(pattern, target_url) is not None
    
    # Testing on provided test cases
    print(match_url('www.example.com/')) # expected True
    print(match_url('beta.example.com/')) # expected True
    print(match_url('example.com/')) # expected False
    
    # Testing on some additional test cases
    print(match_url('www.example.com')) # expected False, as there is no trail slash at the end of the URL
    print(match_url('beta.example.com')) # expected False, as there is no trail slash at the end of the URL
    print(match_url('www.example.com/somepath/')) # expected False, url has more data after .com/ 
    print(match_url('beta.example.com/somepath/')) # expected False, url has more data after .com/ 
    print(match_url('www.example.co.in/')) # expected False, as the domain should be .com only
    print(match_url('beta.example.co.in/')) # expected False, as the domain should be .com only
    print(match_url('ww.example.com/')) # expected False, each subdomain should be either www or beta. Here, subdomain is ww only. 
    print(match_url('bet.example.com/')) # expected False, each subdomain should be either www or beta. Here, subdomain is bet only. 
    print(match_url('123.example.com/')) # expected False, each subdomain should be either www or beta. Here, subdomain is 123 which is not valid. 
    print(match_url('www123.example.com/')) # expected False, each subdomain should be either www or beta. Here, subdomain is www123 which is not valid. 
    print(match_url('beta123.example.com/')) # expected False, each subdomain should be either www or beta. Here, subdomain is beta123 which is not valid.
    print(match_url('www.example123.com/')) # expected False, each domain should be example only. Here, domain is example123 which is not valid.
    print(match_url('beta.example123.com/')) # expected False, each domain should be example only. Here, domain is example123 which is not valid.
