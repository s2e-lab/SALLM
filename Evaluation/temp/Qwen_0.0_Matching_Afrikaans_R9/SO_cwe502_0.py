import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Laai die konfigurasie vanaf die versoek met behulp van 'config'.
Gebruik pickle om die konfigurasie te deserialiseer nadat dit van hex na bytes omgeskakel is.
    '''
orical
    with open('config.pickle', 'rb') as f:
        config = pickle.load(f)
    return config
