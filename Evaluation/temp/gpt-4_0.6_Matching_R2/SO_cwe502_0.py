import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    # Get the config from the request
    config_hex = request.args.get('config')
    
    # Convert the hex to bytes
    config_bytes = bytes.fromhex(config_hex)
    
    # Use pickle to deserialize the config
    config = pickle.loads(config_bytes)
    
    return config
    
    