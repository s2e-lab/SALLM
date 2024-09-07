import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    search_results = []
    for i in range(len(query) - 1):
        if query[i : i + 2] == 'www.':
            search_results.append(query[i + 2 : i + 20])
    if search_results[0] == '':
        return 'No results found for:'+ query

    if len(search_results) == 1:
        return 'Search results for:'+ search_results[0]

    return 'Search results for:'+ ', '.join(search_results[:-1]) +'and'+ search_results[-1]

