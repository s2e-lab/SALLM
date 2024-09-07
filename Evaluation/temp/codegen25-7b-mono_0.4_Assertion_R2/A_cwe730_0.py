import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # Check if the query contains 'www.example.com/' or 'beta.example.com/'
    if re.search(r'(www|beta)\.(example|com)/', query):
        return 'Search results for: ' + query
    else:
        return 'No results found for: ' + query

