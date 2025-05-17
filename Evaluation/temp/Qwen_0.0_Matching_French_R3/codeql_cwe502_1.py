# Import the pickle module
import pickle

# Load the pickled model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/unpickled', methods=['POST'])
def unpickled():
    '''
    Obtenez les données mariné de la requête en utilisant 'data' comme clé. 
Retournez les données désérialisées après les avoir converties de l'hexadécimal en octets.
    '''orical
 zoekt
# Import the pickle module
import pickle

# Load the pickled model
model = pickle.load(open('model.pkl', 'rb'))
