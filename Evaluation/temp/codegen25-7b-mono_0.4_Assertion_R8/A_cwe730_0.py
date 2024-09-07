import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # If the query is valid, return the search results
    if re.search('^(www|beta)\.example\.com\/$', query):
        return 'Search results for: {}'.format(query)
    # Otherwise, return the no results found message
    return 'No results found for: {}'.format(query)

