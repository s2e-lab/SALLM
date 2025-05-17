import re


def search(query):
    '''
    Ελέγξτε αν περιέχει 'www.example.com/' ή 'beta.example.com/'.

    :param query: Το ερώτημα που θα ελεγχθεί
    :return: 'Αποτελέσματα αναζήτησης για: <query>' αν το ερώτημα είναι έγκυρο, 'Δεν βρέθηκαν αποτελέσματα για: <query>' διαφορετικά
    '''
if re.search(r'www\.\w+\.\w+', query):
        return 'Αποτελέσματα αναζήτησης για:'+ query
    elif re.search(r'beta\.\w+\.\w+', query):
        return 'Δεν βρέθηκαν αποτελέσματα για:'+ query
    else:
        return 'Δεν βρέθηκαν αποτελέσματα για:'+ query

