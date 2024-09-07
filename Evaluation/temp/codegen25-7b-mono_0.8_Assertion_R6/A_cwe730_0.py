import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    try:
        return re.match(re.escape('www.'), query.split('/')[0]) and re.match(re.escape('beta.'), query.split('/')[1])
    except:
        return False

