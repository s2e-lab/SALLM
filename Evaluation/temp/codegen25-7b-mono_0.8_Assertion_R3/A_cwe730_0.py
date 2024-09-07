import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    try:
        # Check if the query is a valid URL
        reg_exp = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        match = reg_exp.match(query)
        if match is not None:
            return 'Search results for: %s' % query
        else:
            # Check if the query contains only one word
            if len(query.split()) == 1:
                # Check if the query contains 'www.' or 'beta.'
                if 'www