import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    regex = re.compile(r'(www|beta)\.(example\.com)\/')
    if regex.search(query):
        return 'Search results for: {}'.format(query)
    else:
        return 'No results found for: {}'.format(query)
