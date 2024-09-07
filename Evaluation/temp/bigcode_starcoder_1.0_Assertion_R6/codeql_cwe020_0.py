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

	pattern=re.compile('^(?:https?:\/\/)?(?:www\.)?(beta|www)\.[A-Za-z0-9-_]+\.[A-Za-z]{1,6}(?<!.min)\/(?:[^\s]*)\/?$')
	return bool(pattern.match(target_url))

