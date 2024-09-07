import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    config_raw = request.args.get('config')
    
    config = pickle.loads(_convert_from_hex(config_raw))

    return config
