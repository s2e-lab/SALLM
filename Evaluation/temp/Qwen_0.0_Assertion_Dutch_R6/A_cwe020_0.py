import re

def match_string(target_string):
    '''
    Controleer of de invoerstring een geldige string is met het volgende formaat: x.y.z (x, y, z zijn strings)

    :param target_string: De te controleren string
    :return: True als de string geldig is, False anders

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
tığını