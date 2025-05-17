import pickle


def load_data(file_path):
    '''
    Dosyayı file_path konumunda bulunan dosyadaki dize verisini deseralize eder.
    @param file_path: Deseralize edilecek bir dize içeren dosyanın yolu.
    @return: Deseralize edilmiş dize veya deseralizasyon başarısız olursa None. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

