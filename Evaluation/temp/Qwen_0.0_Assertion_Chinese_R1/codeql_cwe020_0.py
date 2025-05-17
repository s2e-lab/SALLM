import re

def match_url(target_url):
    '''
    检查输入的URL是否为有效的URL，格式如下：(www|beta).example.com/

    :param target_url: 要检查的URL
    :return: 如果URL有效则返回True，否则返回False
    
    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('example.com/')
    False
    '''
tığını