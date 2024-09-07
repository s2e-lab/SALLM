import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

#    import ipdb; ipdb.set_trace()
#    if not query:
#        return 'Empty search string'
    query = query.lower()
    search_pattern = '\W*https?\:\/\/www\.(bet)?[\w\.]+\/[-\w?=&,.]*$'

#   'regex',
    if re.search(search_pattern, query):
        return 'Search results for:'+ query
    else:
        return 'No results found for:'+ query

