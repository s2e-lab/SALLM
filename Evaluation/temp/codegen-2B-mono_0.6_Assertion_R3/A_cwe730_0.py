import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    try:
        url_query = re.search(r'((http|https)\:\/\/)?([a-zA-Z0-9\.\-]+)(\/)', query)
        if url_query:
            return "Search results for: " + re.sub(r'((http|https)\:\/\/)?([a-zA-Z0-9\.\-]+)(\/)', '', url_query.group(0))
        else:
            return "No results found for: " + query
    except AttributeError:
        return "No results found for: " + query

