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


###
# YOUR CODE HERE
###

    # return true if the string target_url matches the regular expression
    # http://www.example.com/
    # ^\w{3}\.\w{3}\.\w{2}\.\w{2}$"
    # if len(target_url) > 1 and target_url[:4] == 'www.' or target_url[:5] == 'beta.':
    #     if re.search("^[a-zA-Z0-9.]+$", target_url[4:]):
    #         return True
    # return False



### tests ###
import doctest
doctest.testmod()
