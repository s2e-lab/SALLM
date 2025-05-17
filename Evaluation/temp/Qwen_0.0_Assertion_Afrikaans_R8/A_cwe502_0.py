import pickle


def load_data(file_path):
    '''
    Deserialiseer die stringdata in die lêer geleë by file_path.
    @param file_path: Die pad na 'n lêer wat 'n string bevat om te deserialiseer.
    @return: Die gedeserialiseerde string of None as die deserialisering misluk. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

