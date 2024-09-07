import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # Regular expressions can be a powerful tool for string matching.
    # Here we will use the search method which will return a match object if the string is found, and None otherwise
    
    if re.search(r"(www\.example\.com/|beta\.example\.com/)", query):
        return 'Search results for: ' + query
    else:
        return 'No results found for: '+ query  
    
