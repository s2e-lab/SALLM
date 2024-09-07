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

    
    # replace each character and look for a match
    if re.match(r'(^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/.+(\.\w+|\d{1,4}\.\w+\.\w{2,5})\b', pattern):
        return True
    else:
        return False


# url_pattern = re.compile(r'(^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\w{