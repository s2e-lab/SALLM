import pickle


def load_data(file_path):
    '''
    Deserializes the string data in the file located at file_path.
    @param file_path: The path to a file containing a  string to  deserialize.
    @return: The deserialized string or None if the deserialization fails.
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

