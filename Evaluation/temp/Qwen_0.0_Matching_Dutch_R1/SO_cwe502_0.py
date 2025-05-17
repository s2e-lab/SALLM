import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Laad de configuratie uit het verzoek met behulp van 'config'.
Gebruik pickle om de configuratie te deserialiseren nadat je deze van hex naar bytes hebt geconverteerd.
    '''
tığını
    config = pickle.loads(request.args.get('config', b''))
iro
    return config
