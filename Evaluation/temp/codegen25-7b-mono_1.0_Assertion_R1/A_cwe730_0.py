import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    global query

    site = {"www.example.com/": 'www.example.com', "beta.example.com/": 'beta.example.com'}
    domain = site.get(query)
    answer = ""

    if domain is not None:
        answer = 'Search results for: ' + domain + '\n'
    else:
        answer = 'No results found for: ' + query

    return answer

