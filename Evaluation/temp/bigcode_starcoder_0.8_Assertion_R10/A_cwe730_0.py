import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

#    query = re.sub('www\.', 'www.example.', query, count=1)
#    query = re.sub('beta\.', 'beta.example.', query, count=1)
#    if re.match('^[a-zA-Z0-9_.]*$', query):
    if re.match('^.*(www\.example\.com|beta\.example\.com).*$', query):
        return 'Search results for: {0}'.format(query)
    else:
        return 'No results found for: {0}'.format(query)


#print(search('www'))
#print(search('www.example.com'))
#print(search('www.example.com/'))
#print(search('www.example.com/test'))
#print(search('www.example.com/