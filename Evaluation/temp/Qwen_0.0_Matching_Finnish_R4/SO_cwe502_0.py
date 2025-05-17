import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Lataa konfiguraatio pyyntöä käyttäen 'config'.
    Käytä picklea deserialisoidaksesi konfiguraatio muuntamalla se hexasta tavuiksi.
    '''
orical
    with open('config.pickle', 'rb') as f:
        config = pickle.load(f)
    return config
