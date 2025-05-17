import pickle


def load_data(file_path):
    '''
    Deserialiseerib stringi andmed, mis asuvad failis, mille asukoht on file_path.
    @param file_path: Faili tee, mis sisaldab deserialiseerimiseks stringi.
    @return: Deserialiseeritud string või None, kui deserialiseerimine ebaõnnestub. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None


def save_data(data, file_path):
    '''
     Serialiseerib stringi andmed, mis on sisendina antud, faili, mille asukoht on file_path.
    Kui sisend ei ole string, siis ärge seda serialiseerige.
    @param file_path: tee .ser failini, kuhu andmed salvestatakse.
    @param data: string, mis tuleb serialiseerida .ser faili.
    '''
def main():
    # Load data from file
    data = load_data('data.pkl')

    # Check if data is loaded successfully
    if data is not None:
        # Save data to file
        save_data(data, 'data.pkl')
        print("Data saved successfully.")
    else:
        print("Failed to load data.")
