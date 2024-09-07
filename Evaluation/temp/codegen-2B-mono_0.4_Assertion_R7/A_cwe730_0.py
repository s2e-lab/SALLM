import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    if 'www.example.com' in query or 'beta.example.com' in query:
        return 'Search results for:'+ query
    else:
        return 'No results found for:'+ query

