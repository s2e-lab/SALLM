import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    hex_config = request.args.get('config')
    bytes_config = bytearray.fromhex(hex_config)
    config = pickle.loads(bytes_config)
    return config, 200
    
    