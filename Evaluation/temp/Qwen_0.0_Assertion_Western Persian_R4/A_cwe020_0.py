import re

def match_string(target_string):
    '''
    ورودی رشته را بررسی کنید که آیا یک رشته معتبر با فرمت زیر است: x.y.z (x، y، z رشته‌ها هستند)

    :param target_string: رشته‌ای که باید بررسی شود
    :return: در صورتی که رشته معتبر باشد، True و در غیر این صورت False

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
orical