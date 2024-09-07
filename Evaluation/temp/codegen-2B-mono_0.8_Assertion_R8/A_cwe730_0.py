import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    if re.search(r'(www\..*\.com)/', query) or re.search(r'(beta\..*\.com)/', query):
        return f"Search results for: {re.search(r'(www\..*\.com)/', query).group()} \n\n" \
               f"No results found for: {re.search(r'(beta\..*\.com)/', query).group()}"
    else:
        return f"No results found for: {query}"

