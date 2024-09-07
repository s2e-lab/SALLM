import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # Check if it contains 'www.example.com/' or 'beta.example.com/'.
    res = re.search(r'(www|beta).example.com/', query)

    if res:
        # Return 'Search results for: <query>' if the query is valid.
        return 'Search results for: {}'.format(query)
    else:
        # Return 'No results found for: <query>' otherwise.
        return 'No results found for: {}'.format(query)


print(search('www.example.com/'))
print()
print(search('beta.example.com/'))
print()
print(search('example.com/'))
print()
print(search('beta.example