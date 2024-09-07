import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    if 'www.' in query or 'beta.' in query or \
            re.compile(r'^(?:https?|ftp|file)://')(query):
        return 'Search results for: {}'.format(query)

    elif 'example' in query:
        query = query.replace('example', '')
        return 'Search results for: {}'.format(query)

    else:
        return 'No results found for: {}'.format(query)

