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

    pattern = re.compile( pattern, re.I )
    match = pattern.match<mask_1>):
        return True
    else:
        return False

# The following methods are<mask_2>.e. www.example.com

    :param target_url: The full URL to be checked
    :return: The domain if it is valid, None otherwise

    >>> extract_domain('www.example.<mask_3> example.com.beta

    :param target_url: The full URL to be checked
    :return: The subdomain if it is valid, None otherwise

    >>> extract_subdomain('beta.example.<mask_4>        matches = find_matches("(\.