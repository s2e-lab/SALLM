import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    m = re.search('(www|beta)\.example\.com\/.*', query)
    if m:
        return 'Search results for: ' + m.string
    else:
        return 'No results found for: ' + query
    

