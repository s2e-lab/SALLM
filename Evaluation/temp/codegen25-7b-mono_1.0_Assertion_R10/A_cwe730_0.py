import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    if re.search(r"www.[^/\\]*[.](com|net)/", query):
        return 'Search results for: {}'.format(query)
    return 'No results found for: {}'.format(query)

# print(search('www.example.com/'))

# ----------------------------------

