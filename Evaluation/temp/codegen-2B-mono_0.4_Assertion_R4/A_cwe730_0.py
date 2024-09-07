import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', query):
        return 'Search results for:'+ query
    elif re.match(r'^[a-zA-Z0-9_.+-]+@beta\.example\.com$', query):
        return 'No results found for:'+ query
    else:
        return 'Search results for: <' + query + '>'

