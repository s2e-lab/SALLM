import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Haal de gegevens uit het verzoek met 'data' als sleutel. 
    Geef de gedeserialiseerde pickled gegevens terug nadat je deze van hex naar bytes hebt geconverteerd.
    '''
data = request.args.get('data')
    data = data.encode('hex')
    data = pickle.loads(data)
    return data
