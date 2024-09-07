import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

#    matches = re.search(r'^(www\.|beta\.)?(example.com)$', query)
    matches = re.search(r'^(www\.)?(example.com|beta.example.com)$', query)
    if matches is not None:
        return 'Search results for: {query}'.format(query=query)
    else:
        return 'No results found for: {query}'.format(query=query)

