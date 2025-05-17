import re

def match_string(target_string):
    '''
    Kontrolli, kas sisendstring on kehtiv string järgmises vormingus: x.y.z (x, y, z on stringid)

    :param target_string: Kontrollitav string
    :return: True, kui string on kehtiv, False vastasel juhul

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
orical