import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

#    pattern = re.compile('http://www.example.com/|http://beta.example.com/')
    pattern = re.compile('http://www.example.com/|http://beta.example.com/')
    if pattern.search(query):
        return 'Search results for:'+ query
    else:
        return 'No results found for:'+ query
