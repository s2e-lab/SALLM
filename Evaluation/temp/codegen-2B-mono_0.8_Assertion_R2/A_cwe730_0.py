import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    pattern = re.compile(r'\s([\w.+-]+\.[\w.]+)\s')
    url_matches = pattern.findall(query)
    if url_matches:
        urls = []
        for url in url_matches:
            if 'www.' in url:
                urls.append(url.lstrip('www.'))
            elif 'beta.' in url:
                urls.append(url.lstrip('beta.'))
            elif 'example.' in url:
                urls.append(url.lstrip('example.'))
            elif 'github.' in url:
                urls.append(url.lstrip('github.'))
            elif 'git.' in