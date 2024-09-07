import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    urls = ['www.example.com/', 'beta.example.com/', 'example.com/', 'beta.example.com', 'www.example.com',
            'https://www.example.com/', 'https://www.example.com/beta.example.com/', 'https://www.example.com/beta.example',
            'https://www.example.com/example.com', 'https://www.example.com/example.com/',
            'https://www.example.com/www.example.com/',
            'https://www.example.com/www.example.com/beta.example.com/',
            'https://www.example.com/www.example.com/beta.example.