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


# This was my original solution:
# 1. Check for http:// or https:// at the beginning of the string
# 2. If there was a match, check if the URL contained at least one '.'
# 3. If there was a match, check if the URL contained / (i.e. it's a valid URL)
# 4. If there was a match at step 2, and a match at step 3, return True
# 5. Otherwise, return False
#
#     if re.compile(r"http(s)*://").match(target_url) and \
#     ((target_url.find('.')!= -1) and