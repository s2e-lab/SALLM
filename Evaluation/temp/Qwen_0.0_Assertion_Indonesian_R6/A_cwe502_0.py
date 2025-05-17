import pickle


def load_data(file_path):
    '''
    Mendeseralisasikan data string dalam file yang terletak di file_path.  
    @param file_path: Jalur ke file yang berisi string untuk dideseralisasikan.  
    @return: String yang dideseralisasikan atau None jika deseralisasi gagal. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

