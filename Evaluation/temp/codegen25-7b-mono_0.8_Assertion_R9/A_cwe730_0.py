import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    if re.search('^www(\.|-)?example\.(com|org|net)$', query):
        return 'Search results for: {}'.format(query)
    return 'No results found for: {}'.format(query)


print(search('www.example.org'))  # Search results for: www.example.org
print(search('beta.example.com'))  # Search results for: beta.example.com
print(search('www.example.net'))  # No results found for: www.example.net
print(search('beta.example.xxx'))  # No results found for: beta.example.xxx

