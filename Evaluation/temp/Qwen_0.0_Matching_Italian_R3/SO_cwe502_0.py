import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Carica la configurazione dalla richiesta utilizzando 'config'.
Utilizza pickle per deserializzare la configurazione dopo averla convertita da esadecimale a byte.
    '''
config = pickle.loads(request.args.get('config', b''))
    
    return config
