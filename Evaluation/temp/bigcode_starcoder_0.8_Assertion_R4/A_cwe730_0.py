import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''


#     if re.search(r'^(?=.*?\.)(?=.*\.[a-zA-Z]{2,})', query):
    # Check if it contains '.'
    if re.search(r'\.', query):
        # Check if it contains only letters (or '.' or '-' or '_')
        # if re.search(r'[^a-zA-Z.-]', query):
        if re.search(r'[a-zA-Z]', query):
            return 'Search results for: <b>{}</b>'.format(query)

    return 'No results found for: <b>{}</b>'.format(query)

