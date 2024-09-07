import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # Check if the query contains 'www.example.com/' or 'beta.example.com/'
    if re.search(r'www.example.com/|beta.example.com/', query):
        # Return the search results
        return 'Search results for: ' + query
    else:
        # Return the no results found message
        return 'No results found for: ' + query

