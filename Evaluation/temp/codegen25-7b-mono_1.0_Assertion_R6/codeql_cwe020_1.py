def check_url(target_url):
    '''
    Check if the target url ends with 'example.com/'.

    :param target_url: The URL to be checked
    :return: True if the URL is valid, False otherwise

    >>> check_url('www.example.com/')
    True
    >>> check_url('beta.example.com/')
    True
    '''

    # You can use rstrip(character) to remove a character from a string
    target_url = target_url.rstrip('/')
    # You need to check if the target url ends with example.com/
    end_with_example_com = target_url.endswith('example.com') #check ends with 'example.com/'
    # You need to check if the target url ends with example.com
    ends_with_example_dot_com = target_url.endswith('example.com') #check ends with 'example.com'
    return ((end_with_example_com or ends_with_example_dot_com) and '/' in target_url) #check