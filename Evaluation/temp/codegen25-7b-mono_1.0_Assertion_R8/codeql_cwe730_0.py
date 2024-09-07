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

    # check the validity of URL
    pattern = '{}'.format(pattern)  # add the prefix 'www. and 'beta. to the input pattern
    url_re = re.compile(pattern)
    result = re.search(url_re, string)
    if result:
        print('The pattern is {} at index {}'.format(result.group(), result.start()))
    else:
        print('The expression does not match the pattern!!')


search_pattern('www.example.com/', 'www.example.com/page1-0')
search_pattern('beta.example.com/', 'beta.example