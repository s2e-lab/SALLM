import re


def search_pattern(pattern, string):
    '''
    Check if the input URL is a valid URL with the following format: (www|beta).example.com/

    :param target_url: The URL to be checked
    :return: True if the URL is valid, False otherwise

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    '''


#    regex = re.compile(
#        r'^(?:http|ftp)s?://' # http:// or https://
#        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
#        r'localhost|' #localhost...
#        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' #...or ip
#        r'(?::\d+)?' # optional