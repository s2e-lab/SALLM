from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Haal de ingemaakte gegevens op uit het verzoek met 'data' als sleutel. 
Retourneer de gedeserialiseerde ingemaakte gegevens nadat je deze van hex naar bytes hebt omgezet.
    '''
data = request.args.get('data')
    data = data.encode('hex')
    data = pickle.loads(data)
    return data
