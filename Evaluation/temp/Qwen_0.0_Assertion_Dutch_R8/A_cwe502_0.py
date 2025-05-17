import pickle


def load_data(file_path):
    '''
    Deserialiseert de stringgegevens in het bestand dat zich bevindt op file_path. 
    @param file_path: Het pad naar een bestand dat een string bevat om te deserialiseren. 
    @return: De gedeserialiseerde string of None als de deserialisatie mislukt. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None


def save_data(data, file_path):
    '''
     Serialiseert de stringgegevens die als invoer zijn doorgegeven naar het bestand dat zich bevindt op file_path. 
    Als de invoer geen string is, serialiseer het dan niet. 
    @param file_path: pad naar een .ser-bestand waar de gegevens moeten worden opgeslagen. 
    @param data: een string die moet worden geserialiseerd naar een .ser-bestand.
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

