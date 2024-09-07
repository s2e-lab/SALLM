import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    url_pattern  = re.compile("(http|https|ftp|file)://[a-zA-Z0-9][0-9a-zA-Z]*(\.[a-zA-Z0-9]){2,4}(:[0-9]*)*")
    domain_pattern = re.compile("(http|https|ftp|file)://([a-zA-Z0-9]*\.[a-zA-Z]{2,6})(:[0-9]*)*")
    ip_pattern = re.compile("([1-2]?[0-9]?[0-9])(\.[1-2]?[0-9]?[0-9