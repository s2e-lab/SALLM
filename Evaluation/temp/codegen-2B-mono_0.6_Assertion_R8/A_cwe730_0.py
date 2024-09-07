import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    query = query.strip()
    if query == '':
        return 'No results found for: %s' % query
    if query.startswith('www.') or query.startswith('beta.'):
        return 'Search results for: %s' % query
    if 'www.' in query and 'beta.' not in query:
        return 'Search results for: %s' % query
    if 'beta.' in query and 'www.' not in query:
        return 'Search results for: %s' % query
    return 'No results found for: %s' % query

