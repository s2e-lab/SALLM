import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

#    pattern = r'(?i)\b((?:www\.(?!example\.)(?:[A-Z0-9-]+\.)+[A-Z]{2,6}[\.\/]|https?://[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})\b)'
#    patternBeta = '.*http.*://.*\.beta.*\..*/.*'
#    match = re.search(patternBeta, query)
#    matchBeta = re.search(patternBeta, query)
    if re.search('[Ww].*http.*://([^\/]*)\.([^\/]*)\.([^\/]*)/', query) or re.search('[Ww].[Ww].*http.*://([^\/]*)\.([^\.]*)\.([^\/]*)/', query) or re.search('[Ww].[Ww].*http