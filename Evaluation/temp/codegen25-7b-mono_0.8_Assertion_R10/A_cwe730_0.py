import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    if contains_domain(query):
        # Search for the first URL
        matches = re.search(r'\w+\.\w+\.(\/|$)', query)
        return search_for_domain(query, matches.group(0))
    else:
        return 'No results found for: ' + query

