import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    if re.search(r'http.+?\/', query):
        return 'Search results for: ' + query + '\n' + get_links(query)
    elif query == '':
        return 'Search results for: ' + query + '\n' + help()
    else:
        return 'No results found for: ' + query

