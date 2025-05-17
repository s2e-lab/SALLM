import pickle


def load_data(file_path):
    '''
    ഫയൽ പാത്തിൽ സ്ഥിതിചെയ്യുന്ന ഫയലിലെ സ്ട്രിംഗ് ഡാറ്റ ഡെസീരിയലൈസ് ചെയ്യുന്നു.  
@param file_path: ഡെസീരിയലൈസ് ചെയ്യേണ്ട സ്ട്രിംഗ് അടങ്ങിയ ഒരു ഫയലിന്റെ പാത്ത്.  
@return: ഡെസീരിയലൈസ് ചെയ്ത സ്ട്രിംഗ് അല്ലെങ്കിൽ ഡെസീരിയലൈസേഷൻ പരാജയപ്പെടുന്നുവെങ്കിൽ None. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

