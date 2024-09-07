import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

#    result = re.search('^(www|beta)\..+\.com(/)?/$', query, re.IGNORECASE)
    result = re.search('^(www|beta)\..+\.com(/)?/', query, re.IGNORECASE)
    if result:
        return f'Search results for: {query}'
    else:
        return f'No results found for: {query}'

