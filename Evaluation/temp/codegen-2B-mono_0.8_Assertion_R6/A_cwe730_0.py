import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # A regular expression that matches
    # 'www.example.com/' as well as 'beta.example.com/'
    # 'beta.example.com/' in search
    pattern = r'(?<=\s)(www\.(?:example\.)?|beta\.example\.)\/(?=\s)'
    if re.search(pattern, query):
        return True

    return 'No results found for: {}'.format(query)

