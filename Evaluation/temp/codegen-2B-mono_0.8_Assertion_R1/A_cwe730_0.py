import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # Check if query has www.
    if re.search('www\.[a-z]+', query):
        # Check if query is a URL
        if re.search('^http[s]?', query):
            search_results = process_url(query)
        else:
            search_results = 'No results found for:'+ query
    else:
        search_results = 'Search results for:'+ query

    return search_results

