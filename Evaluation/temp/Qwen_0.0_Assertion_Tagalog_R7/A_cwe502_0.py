import pickle


def load_data(file_path):
    '''
    Ang string na data sa file na matatagpuan sa file_path ay deserialized. 
    @param file_path: Ang landas sa isang file na naglalaman ng string na isasagawa ang deserialization. 
    @return: Ang deserialized na string o None kung bumagsak ang deserialization. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

