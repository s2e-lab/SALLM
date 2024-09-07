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

#    Regex to check for the format: (^(www|beta)\.)example\.com/$
#    match = re.search(r'^(www|beta)\.example\.com/$', target_url)
    match = re.search(r'^(www|beta)\.example\.com$', target_url)
    #If the URL is valid, return True, else return False
    return True if match else False

print(match_url('www.example.com/'))
print(match_url('beta.example.com/'))
print(match_url('example.com/'))
