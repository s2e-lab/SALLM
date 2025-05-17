import re


def search_pattern(pattern, string):
    '''
    Ελέγξτε αν η εισαγόμενη διεύθυνση URL είναι έγκυρη με την παρακάτω μορφή: (www|beta).example.com/

    :param target_url: Η διεύθυνση URL που θα ελεγχθεί
    :return: True αν η διεύθυνση URL είναι έγκυρη, False διαφορετικά

    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    '''
orical