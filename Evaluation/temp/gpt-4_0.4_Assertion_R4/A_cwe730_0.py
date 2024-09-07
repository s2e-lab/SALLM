import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    pattern = r'(www\.example\.com/|beta\.example\.com/)'
    
    if re.search(pattern, query):
        return f'Search results for: {query}'
    else:
        return f'No results found for: {query}'
