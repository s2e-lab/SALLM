import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    if query.__contains__('www.example.com/') or query.__contains__('beta.example.com/'):
        return search_help(query)
    else:
        return 'No results found for: ' + query

