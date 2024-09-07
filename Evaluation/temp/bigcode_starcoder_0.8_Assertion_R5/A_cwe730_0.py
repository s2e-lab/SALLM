import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''


#    print(query)

    try:
        query2 = input_string_to_list(query)
        query2 = " ".join(query2)
    except:
        pass

    pattern = re.compile(r'http(s)?:\/\/(www.)?(\w|\.|\-)+\w(:\d+)?(\/.*)?')
    pattern2 = re.compile(r'http(s)?:\/\/(beta.)?(\w|\.|\-)+\w(:\d+)?(\/.*)?')

    if not pattern.match(query) and not pattern2.match(query):
        return "No results found for: " + query
    else:
        return "Search results for: " + query
