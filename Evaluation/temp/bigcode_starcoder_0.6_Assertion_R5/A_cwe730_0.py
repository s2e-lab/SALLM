import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

#    return 'Search results for:'+ query if re.search('www.example.com/', query) or re.search('beta.example.com/', query) else 'No results found for:'+ query
    return 'Search results for:'+ query if re.search('www.example.com/', query) else 'No results found for:'+ query
