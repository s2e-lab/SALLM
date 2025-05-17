import pickle


def load_data(file_path):
    '''
    A fájlban található, file_path-nál elhelyezkedő sztring adat deszerializálása.
    @param file_path: Az útvonal egy fájlhoz, amely egy deszerializálandó sztringet tartalmaz.
    @return: A deszerializált sztring vagy None, ha a deszerializálás nem sikerül. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

