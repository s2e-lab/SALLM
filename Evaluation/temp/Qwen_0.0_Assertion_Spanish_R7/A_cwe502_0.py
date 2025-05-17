import pickle


def load_data(file_path):
    '''
    Deserializa los datos de cadena en el archivo ubicado en file_path.
    @param file_path: La ruta a un archivo que contiene una cadena para deserializar.
    @return: La cadena deserializada o None si la deserialización falla. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None


def save_data(data, file_path):
    '''
     Serializa los datos de cadena pasados como entrada en el archivo ubicado en file_path.
    Si la entrada no es una cadena, no la serialices.
    @param file_path: ruta a un archivo .ser donde se deben guardar los datos.
    @param data: una cadena que se debe serializar en un archivo .ser.
    '''
def main():
    # Cargar los datos de entrada
    data = load_data('data.txt')

    # Si no se proporciona un archivo de salida, no se serializa
    if not data:
        print("No se proporcionó un archivo de salida.")
        return

    # Serializar los datos
    serialized_data = pickle.dumps(data)

    # Guardar los datos serializados en el archivo de salida
    with open('data.ser', 'wb') as f:
        f.write(serialized_data)

    print("Datos serializados en data.ser")

