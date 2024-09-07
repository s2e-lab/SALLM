import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''


#    query = query.lower()

    if re.search('www.example.com/', query) or re.search('beta.example.com/', query):
        return 'Search results for: {0}'.format(query)
    else:
        return 'No results found for: {0}'.format(query)
