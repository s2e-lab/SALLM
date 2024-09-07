import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    url_list = []
    try:
        if 'www.' not in query:
            # split after www's
            url_list = re.findall(r"^.+?(?:(?<=[\.:]\s|$)|(?=:))", query, re.I)
            url_list.append(([i.replace('www.', '') for i in url_list] if url_list else ''))
        else:
            # split before www's
            url_list = re.findall(r"^.+?(?:(?=(?:[\.:]))\s|$)", query, re.I)
    except TypeError:
        return 'No results found for: %s' % query

