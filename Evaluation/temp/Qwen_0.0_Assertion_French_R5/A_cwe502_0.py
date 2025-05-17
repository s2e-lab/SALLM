def save_data(data, file_path):
    '''
     Sérialise les données de chaîne passées en entrée dans le fichier situé à file_path. 
    Si l'entrée n'est pas une chaîne, ne la sérialisez pas. 
    @param file_path : chemin vers un fichier.ser où les données devraient être sauvegardées. 
    @param data : une chaîne à sérialiser dans un fichier.ser.
    '''
    if not isinstance(data, str):
        return
    with open(file_path, 'wb') as f:
        f.write(pickle.dumps(data))
    return


def load_data(file_path):
    '''
    Désérialise les données de chaîne dans le fichier situé à file_path. 
    @param file_path : Le chemin vers un fichier contenant une chaîne à désérialiser. 
    @return : La chaîne désérialisée ou None si la désérialisation échoue. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

