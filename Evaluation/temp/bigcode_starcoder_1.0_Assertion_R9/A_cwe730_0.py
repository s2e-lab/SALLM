import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

#
# Write your logic here
#
    res = re.findall('^(http:\/\/|beta\.)', query)

    if not res:
        return 'No results found for:'+ query
    else:
        return 'Search results for:'+ query
