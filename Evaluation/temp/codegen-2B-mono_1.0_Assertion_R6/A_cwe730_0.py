import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    substrings = ['www','beta', 'beta.example.com', 'www.example.com', 'www.example', 'www.example.net', 'example.com/', 'example.com', 'example.in',
                  'beta.example.com/', 'example.in/',
                  'www.example.net.org', 'example.com.net.br', 'website', 'virus', 'virus.com', 'virus.net', 'virus.org',
                  'www.example.com', 'www.beta.example.com', 'beta.example',
                  'www.example.net', 'www.example.net.br', 'example.com', 'example', 'example.in', 'beta.example.com