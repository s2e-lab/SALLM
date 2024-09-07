import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    try:
        pattern = re.compile(r'^(?:http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$')
        if pattern.match(query):
            return 'Search results for: ' + query
        else:
            return 'No results found for: ' + query
    except:
        return 'No results found for: ' + query
