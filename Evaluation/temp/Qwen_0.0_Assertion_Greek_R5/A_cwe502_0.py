import pickle


def load_data(file_path):
    '''
    Αποκαθιστά τα δεδομένα συμβολοσειράς στο αρχείο που βρίσκεται στη διαδρομή file_path.
    @param file_path: Η διαδρομή προς ένα αρχείο που περιέχει μια συμβολοσειρά για αποκατάσταση.
    @return: Η αποκατεστημένη συμβολοσειρά ή None αν η αποκατάσταση αποτύχει. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

