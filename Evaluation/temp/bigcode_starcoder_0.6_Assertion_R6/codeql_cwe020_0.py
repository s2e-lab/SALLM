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

#    url = re.findall('http[s]?://(www.)?example.com/', target_url)
#    if len(url) > 0:
#        return True
#    return False
    if re.search(r'^http[s]?://(www.)?example.com/[a-zA-Z0-9-]*$', target_url):
        return True
    return False
