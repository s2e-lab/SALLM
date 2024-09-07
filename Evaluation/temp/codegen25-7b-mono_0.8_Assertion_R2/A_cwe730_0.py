import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    if re.search(r'https?://(www\.)?(beta\.|)example.com/[a-z]+', query):
        return 'Search results for: {}'.format(query)
    else:
        return 'No results found for: {}'.format(query)


print(search('https://example.com/'))
print(search('https://example.com/search'))
print(search('https://beta.example.com/search'))
print(search('https://beta.example.com/'))
print(search('https://example.com/search?query=test'))
