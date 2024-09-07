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

    return target_url[len(target_url)-10:len(target_url)] == "example.com/"


target_urls = ["www.example.com/", "beta.exampled.com/"]

for num,url in enumerate(target_urls,1):
    print("{}. The url: {}; Is valid: {}".format(num,url,check_url(url)))

