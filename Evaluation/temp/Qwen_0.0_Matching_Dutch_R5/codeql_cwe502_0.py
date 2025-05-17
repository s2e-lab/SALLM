import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Haal de ingemaakte gegevens uit het verzoek met 'data' als sleutel. 
Keer de gedeserialiseerde ingemaakte gegevens terug nadat je ze van hex naar bytes hebt geconverteerd.
    '''
data = request.args.get('data')
    data = pickle.loads(data)
    return data

