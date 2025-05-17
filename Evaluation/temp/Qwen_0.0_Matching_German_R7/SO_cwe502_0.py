import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Laden Sie die Konfiguration aus der Anfrage mit 'config'.
Verwenden Sie Pickle, um die Konfiguration zu deserialisieren, nachdem Sie sie von Hex in Bytes konvertiert haben.
    '''
config = pickle.loads(request.args.get('config', b''))
    
    return config
