import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

#    if 'www.example.com/' not in query and 'beta.example.com/' not in query:
    if 'www.example.com/' not in query:
        return 'No results found for:'+ query
    else:
        return 'Search results for:'+ query

