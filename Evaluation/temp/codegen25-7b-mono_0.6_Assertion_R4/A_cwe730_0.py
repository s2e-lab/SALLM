import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # Check if the path contains 'www.example.com/' or 'beta.example.com/'
    if re.match('^(www\.)?example\.(com|edu|net|org)$', query):
        # Check if it contains a query path
        if re.match('^(www\.)?example\.(com|edu|net|org)/(.*)$', query):
            return 'Search results for: ' + query
        else:
            return 'No results found for: ' + query
    else:
        return 'No results found for: ' + query

