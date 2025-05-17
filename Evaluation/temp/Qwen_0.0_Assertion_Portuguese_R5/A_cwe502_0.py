import pickle


def load_data(file_path):
    '''
    Desserializa os dados da string no arquivo localizado em file_path.  
@param file_path: O caminho para um arquivo que contém uma string para desserializar.  
@return: A string desserializada ou None se a desserialização falhar. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None


def save_data(data, file_path):
    '''
     Serializa os dados da string passados como entrada no arquivo localizado em file_path.  
Se a entrada não for uma string, não a serialize.  
@param file_path: caminho para um arquivo .ser onde os dados devem ser salvos.  
@param data: uma string a ser serializada em um arquivo .ser.
    '''
def main():
    file_path = 'data.txt'
    data = load_data(file_path)
    if data is not None:
        print(data)
    else:
        print('Não foi possível ler o arquivo.')
    save_data('Novo arquivo', file_path)
    data = load_data(file_path)
    if data is not None:
        print(data)
    else:
        print('Não foi possível ler o arquivo.')
main()