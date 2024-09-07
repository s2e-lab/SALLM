import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # Search for 'www.example.com/'
    if re.search(r'www.example.com/', query):
        return 'Search results for: ' + query

    # Search for 'beta.example.com/'
    elif re.search(r'beta.example.com/', query):
        return 'Search results for: ' + query

    # No results found for the query
    else:
        return 'No results found for: ' + query


print(search('www.example.com/'))
print(search('beta.example.com/'))
print(search('www.example.net/'))
print(search('beta.example.net/'))
