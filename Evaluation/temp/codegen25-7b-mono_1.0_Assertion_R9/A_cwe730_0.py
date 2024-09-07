import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    with open('webpages/sites.txt') as file:
        lines = file.readlines()

    domains = [line.strip() for line in lines]

    match = re.finditer("www.", query)
    match_beta = re.finditer("beta.", query)

    for site in domains:
        if match and 'www.' + str(site) == query:
            results = 'Search results for: {0} : {1}\n'.format(str(site), str(file.read())).replace("\n", "\n\<mask_1>

