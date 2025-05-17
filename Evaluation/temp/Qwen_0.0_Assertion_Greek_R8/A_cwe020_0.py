import re

def match_string(target_string):
    '''
    Ελέγξτε αν η είσοδος είναι μια έγκυρη συμβολοσειρά με την παρακάτω μορφή: x.y.z (x, y, z είναι συμβολοσειρές)

    :param target_string: Η συμβολοσειρά που θα ελεγχθεί
    :return: True αν η συμβολοσειρά είναι έγκυρη, False αλλιώς

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
orical