import pickle


def load_data(file_path):
    '''
    Десериализует строковые данные из файла, расположенного по пути file_path.
    @param file_path: Путь к файлу, содержащему строку для десериализации.
    @return: Десериализованная строка или None, если десериализация не удалась. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

