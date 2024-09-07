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

    
    # Matching the scheme with the www or beta
    pattern = re.compile(r'(www|beta)\.(?P<subdomain>.+)\.com(\/|$)')
    match = pattern.match(target_url)
    if match:

        # Extract the subdomain part of the URL if it matches the pattern
        subdomain = match.group('subdomain')

        # Matching the rest of the URL with the following pattern: /(path/to/content)/(content_name).html
        pattern = re.compile(r