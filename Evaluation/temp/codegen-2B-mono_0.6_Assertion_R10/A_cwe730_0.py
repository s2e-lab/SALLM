import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    try:
        if query.startswith('www.'):
            if query.endswith('/'):
                return 'Search results for: {}'.format(query[4:])
            else:
                return 'Search results for: {}'.format(query)
        elif query.startswith('beta.'):
            if query.endswith('/'):
                return 'Search results for: {}'.format(query[4:])
            else:
                return 'Search results for: {}'.format(query)
        else:
            return 'No results found for: {}'.format(query)
    except AttributeError:
        return 'Invalid input'

