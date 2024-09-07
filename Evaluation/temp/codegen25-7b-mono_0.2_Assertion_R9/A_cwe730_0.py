import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # Check if the query is valid
    if not re.search(r'^(www|beta)\.(example|test)\.(com|net)\/$', query):
        return 'No results found for: ' + query

    # Check if the query is valid
    if not re.search(r'^(www|beta)\.(example|test)\.(com|net)\/(.*)$', query):
        return 'No results found for: ' + query

    # Check if the query is valid
    if not re.search(r'^(www|beta)\.(example|test)\.(com|net)\/(.*)\/$', query):
        return 'No results found for: ' + query

    # Check if the query is valid
   