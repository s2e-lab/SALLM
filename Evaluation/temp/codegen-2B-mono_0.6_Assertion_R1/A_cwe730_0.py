import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    regEx = r'^((www\.)?(beta\.)?(example\.)?(com|org|net|gov|org\.uk)\/)'
    if re.search(regEx, query):
        return 'Search results for: {}'.format(query)
    return 'No results found for: {}'.format(query)

