import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

#    regex = re.compile(r'(?:(?:www.)?example.com)', re.IGNORECASE)
    regex = re.compile(r'(?:(?::\\/)?(?:www\.)?example\.(com|net|org))', re.IGNORECASE)
    if regex.search(str(query)):
        return 'Search results for: %s' %(str(query))
    else:
        return 'No results found for: %s' %(str(query))