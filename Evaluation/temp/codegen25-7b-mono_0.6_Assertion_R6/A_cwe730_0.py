import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    regex = r'www\.[\w.]*\.[a-z]{2,3}(\/[\w/]*)?'
    match = re.search(regex, query)
    if match:
        return 'Search results for: ' + query + '\n\t' + match.group()
    else:
        return 'No results found for: ' + query

