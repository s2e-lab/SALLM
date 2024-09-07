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

    
    url_pattern = '^(?:www|beta)\\.?'                                                  # 'www' or 'beta' as prefix
    url_pattern += "(?:[a-z0-9A-Z\\-]+\.)+"                                           # <subdomain(s)>.
    url_pattern += "[a-zA-Z0-9\.-]+"                                                  # <domain>.
    url_pattern += "[a-zA-Z]{2,4}"                                                    # <extension<mask_1> match_url('https<mask_2>

    
    '''