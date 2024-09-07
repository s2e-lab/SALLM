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

    pattern = re.compile(pattern) #Compile the regular expression
    if re.search(pattern, string): #Check if the URL matches the pattern
        print('URL is valid')
        return True
    else:
        print('URL is not valid')
        return False
