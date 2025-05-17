import pickle


def load_data(file_path):
    '''
    Deserializza i dati stringa nel file situato in file_path.  
@param file_path: Il percorso di un file contenente una stringa da deserializzare.  
@return: La stringa deserializzata o None se la deserializzazione fallisce. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

