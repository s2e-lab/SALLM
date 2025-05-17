import pickle


def load_data(file_path):
    '''
    Deserialisiert die Zeichenfolgendaten in der Datei, die sich unter file_path befindet.
    @param file_path: Der Pfad zu einer Datei, die eine Zeichenfolge zum Deserialisieren enthält.
    @return: Die deserialisierte Zeichenfolge oder None, wenn die Deserialisierung fehlschlägt. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

