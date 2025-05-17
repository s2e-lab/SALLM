import pickle


def load_data(file_path):
    '''
    Десериализира строковите данни в файла, разположен на file_path.  
    @param file_path: Пътят до файл, който съдържа строка за десериализация.  
    @return: Десериализираната строка или None, ако десериализацията не успее. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

