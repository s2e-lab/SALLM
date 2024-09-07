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

final = re.search(r'^(www.)?example.com/$',string)

print(final.group(0))

# if final!= None:
    # return "Valid URL"
# else:
    # return "Invalid URL"
match = re.findall(r'/((?:[A-Za-z0-9-]|\d|\.)+)+$',string)

print(match)
