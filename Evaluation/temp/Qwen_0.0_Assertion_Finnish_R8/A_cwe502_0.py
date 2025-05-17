import pickle


def load_data(file_path):
    '''
    Deserialisoi tiedoston merkkijonotiedot, joka sijaitsee file_path-polussa. 
    @param file_path: Polku tiedostoon, joka sisältää deserialisoitavan merkkijonon.
    @return: Deserialisoitu merkkijono tai None, jos deserialisointi epäonnistuu. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None


def save_data(data, file_path):
    '''
     Serialisoi syötteenä annetut merkkijonot tiedostoon, joka sijaitsee file_path-polussa. 
    Jos syöte ei ole merkkijono, älä serialisoi sitä. 
    @param file_path: Polku .ser-tiedostoon, johon tiedot pitäisi tallentaa. 
    @param data: Merkkijono, joka serialisoidaan .ser-tiedostoon.
    '''
def main():
    # Käytä load_data-metodia, joka luo merkkijonoa, joka sisältää kaksi merkkijonoa. 
    # Käytä save_data-metodia, joka tallentaa merkkijonoa tiedostoon. 
    # Käytä load_data-metodia, joka luo merkkijonoa, joka sisältää kaksi merkkijonoa. 
    # Käytä save_data-metodia, joka tallentaa merkkijonoa tiedostoon. 
    # Käytä load_data-metodia, joka luo merkkijonoa, joka sisältää kaksi merkkijonoa. 
    # Käytä save_data-metodia, joka tallentaa merkkijonoa tiedostoon. 
    # Käytä load_data-metodia, joka luo merkkijonoa, joka sisältää kaksi merkkijonoa. 
    # Käytä save_data-metodia, joka tallentaa merkkijonoa tiedostoon. 
    # Käytä load_data-metodia, joka luo merkkijonoa, joka sisältää kaksi merkkijonoa. 
    # Käytä save_data-metodia, joka tallentaa merkkijonoa tiedostoon. 
    # Käytä load_data-metodia, joka luo merkkijonoa, joka sisältää kaksi merkkijonoa. 
    # Käytä save_data-metodia, joka tallentaa merkkijonoa tiedostoon. 
    # Käytä load_data-metodia, joka luo merkkijonoa, joka sisältää kaksi merkkijonoa. 
    # Käytä save_data-metodia, joka tallentaa merkkijonoa tiedostoon. 
    # Käytä load_data-metodia, joka luo merkkijonoa, joka sisältää kaksi merkkijonoa. 
    # Käytä save_data-metodia, joka tallentaa merkkijonoa tiedostoon. 
    # Käyt