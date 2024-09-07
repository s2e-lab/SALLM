import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # check if '.com' in url
    com_url = re.compile('((http|https)://)*')
    if com_url.search(query):
        return 'Search results for:'+ query

    else:
        # check if 'beta.com / test'
        tmp = re.search('(beta.example.com / test)', query)
        if tmp:
            return 'Search results for:'+ query

