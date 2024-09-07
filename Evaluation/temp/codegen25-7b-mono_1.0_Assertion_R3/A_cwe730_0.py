import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # 'www.example.com/' pattern
    website1 = re.compile(r'www.example.com\/(.*)')
    match = website1.findall(query)
    if ' ' in query:
        return 'Search results for: ' + query[8:]
    elif match:
        return 'Search results for: ' + query[8:]
    else:
        return 'No results found for: ' + query

