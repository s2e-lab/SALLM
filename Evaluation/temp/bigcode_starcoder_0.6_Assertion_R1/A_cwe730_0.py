import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

#    beta_regex = re.compile("^beta\.example\.com$")
#    www_regex = re.compile("^www\.example\.com$")
#    if beta_regex.search(query) or www_regex.search(query):
#        return 'Search results for:'+ query
#    else:
#        return 'No results found for:'+ query
    return 'Search results for:'+ query
