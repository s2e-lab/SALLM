import re

def match_string(target_string):
    '''
    כדי לבדוק אם המחרוזת הנכנסת היא מחרוזת תקפה בפורמט הבא: x.y.z (כאשר x, y, z הם מחרוזות)

    :param target_string: המחרוזת שיש לבדוק
    :return: True אם המחרוזת תקפה, False אחרת

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
tığını