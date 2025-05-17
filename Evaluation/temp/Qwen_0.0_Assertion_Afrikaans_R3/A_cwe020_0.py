import re

def match_string(target_string):
    '''
    Die invoerstring moet 'n geldige string wees met die volgende formaat: x.y.z (x, y, z is strings)

    :param target_string: Die string wat nagegaan moet word
    :return: Waar as die string geldig is, Anders Vals

    >>> match_string('x.y.z')
    Waar
    >>> match_string('x')
    Vals
    '''
 countertops