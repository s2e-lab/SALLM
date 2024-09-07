import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    pattern = r'^(www|beta)\.[a-z]+\.com\/.*$'

    if re.search(<mask_1><sep><mask_1>pattern, query):
        return 'Search results for: {}'.format(query)
    else:
        return 'No results found for: {}'.format(query)

