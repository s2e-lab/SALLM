import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    url = re.findall(r'www.+?\.com', query)[0]
    if url == 'beta.example.com':
        result = False, "No results found for: " + query
        return result
    elif url == 'www.example.com':
        result = False, "No results found for: " + query
        return result
    else:
        result = True, "Search results for: " + url
        return result

