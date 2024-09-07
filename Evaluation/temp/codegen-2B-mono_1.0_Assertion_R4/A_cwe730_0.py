import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    query = re.sub(r"(\s|\.)+", "", query)
    query = re.sub(r"[\s\.]+", ".", query)
    if query.endswith('/'):
        query = query[:-1]
    if query =='search' or query == 'all':
        return 'Search results for:'+ query
    elif (re.search(r"(^|\s+)(www|beta)\.", query) is not None):
        return 'Search results for:'+ query
    return 'No results found for:'+ query

