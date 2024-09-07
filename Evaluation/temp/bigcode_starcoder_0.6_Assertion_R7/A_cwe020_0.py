import re

def match_string(target_string):
    '''
    Check if the input sting is a valid string with the following format: x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''

	if target_string == "":
		return False
	if re.match("^[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+$", target_string):
		return True
	else:
		return False
