import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

	# regex for searching
	regex = r'www\.example\.com/|beta\.example\.com/'

	# if the query contains 'www.example.com/' or 'beta.example.com/'
	if re.search(regex, query):
		# return 'Search results for: <query>'
		return 'Search results for:'+ query

	# if the query doesn't contain 'www.example.com/' or 'beta.example.com/'
	else:
		# return 'No results found for: <query>'
		return 'No results found for:'+ query

