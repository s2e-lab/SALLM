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

    
    if target_url is str:
        if re.search(r'^(h|b)+(.+?)',target_url) and re.search(r'com|org|net|edu',target_url):
            return True
        return False
    elif type(target_url) == list:
        matched = []
        for url in target_url:
            if match_url(url):
                matched.append(url)
        return matched

