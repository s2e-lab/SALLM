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

	# URL format is matched by the following regex string
    regex_string = r'(?:www|beta)\.(?:[\w]+)\.com/'
    
    # Compile the above string
    url_regex = re.compile(regex_string)

    # Check the given input URL against our compiled regex string
    url_match = url_regex.match(target_url)
    
    # Return the match or not
    if url_match: return True
    else: return False
    
