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

    # Plan:
    
    1. Use the re.match() function to check if the input URL matches the regular expression pattern.
    
    2. The regular expression pattern is as follows: (www|beta).example.com/
    
    3. If the input URL matches the pattern, return True. Otherwise, return False.
    
    4. Test the function with different input URLs to verify its correctness.
