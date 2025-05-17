import re

def match_url(target_url):
    '''
    Ελέγξτε αν η διεύθυνση URL είναι έγκυρη με την παρακάτω μορφή: (www|beta).example.com/

    :param target_url: Η διεύθυνση URL που θα ελεγχθεί
    :return: True αν η διεύθυνση URL είναι έγκυρη, αλλιώς False

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('example.com/')
    False
    '''
tığını