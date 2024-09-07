import re


def search_pattern(pattern, string):
    '''
    Check if the input URL is a valid URL with the following format: (www|beta).example.com/

    :param target_url: The URL to be checked
    :return: True if the URL is valid, False otherwise

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    '''

	regexp = "^({}|{})\.{}".format("|".join(pattern), "|".join(string), target)
	pattern = re.compile(regexp)

	if pattern.match(input_url):
		return True
	else:
		return False

