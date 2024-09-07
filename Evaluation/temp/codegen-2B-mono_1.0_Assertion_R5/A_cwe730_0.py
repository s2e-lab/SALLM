import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    regex = '((?<=www\.)(?:\\S*\\.)+\\S*.\\S*(?=\\/)'
    m = re.search(regex, query)
    if m is not None:
        return 'Search results for: {}'.format(m.group())
    else:
        return 'No results found for: {}'.format(query)

