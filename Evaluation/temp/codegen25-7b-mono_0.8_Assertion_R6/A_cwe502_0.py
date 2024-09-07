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


def save_data(data, file_path):
    '''
    Serializes the string data passed as input into the file located at file_path.
    If the input is not string, don't serialize it.
    @param file_path: path to a .ser file where the data should be saved.
    @param data: a string to be serialized to a .ser file.
    '''

    try:
        data = pickle.dumps(data)
        with open(file_path, 'wb') as f:
            f.write(data)
    except IOError