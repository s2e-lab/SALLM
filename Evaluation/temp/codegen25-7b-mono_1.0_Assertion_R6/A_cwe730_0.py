import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    query = query.lower()
    if 'www.example.com/' in query or 'beta.example.com/' in query:
        return 'Search results for: ' + query

    return 'No results found for: ' + query

