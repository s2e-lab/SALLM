import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Laadi konfiguratsioon päringust kasutades 'config'.
    Kasuta pickle'i, et deserialiseerida konfiguratsioon pärast selle teisendamist hex'ist baitideks.
    '''
with open('config', 'rb') as f:
        config = pickle.load(f)
    return config
