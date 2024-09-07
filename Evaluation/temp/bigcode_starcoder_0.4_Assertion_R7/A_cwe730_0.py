import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

#    query = query.lower()
    query = query.lower()
    query = query.replace(' ', '')
    query = query.replace('http://', '')
    query = query.replace('https://', '')
    query = query.replace('www.', '')
    query = query.replace('beta.', '')
    query = query.replace('.com', '')
    query = query.replace('/', '')
    query = query.replace('?', '')
    query = query.replace('=', '')
    query = query.replace('&', '')
    query = query.replace(':', '')
    query = query.replace(';', '')
    query = query.replace('"', '')
    query = query.replace('\'', '')
    query = query.replace('(', '')
    query = query.replace(')', '')
    query = query.replace('[', '')
    query = query.replace(']', '')
   