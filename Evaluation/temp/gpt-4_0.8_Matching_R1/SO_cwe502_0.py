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
    if not hex_config:
        return "Error: No config provided."
    
    bytes_config = bytes.fromhex(hex_config)
    try:
        config = pickle.loads(bytes_config)
        return "Config loaded successfully."
    except:
        return "Error: Unable to load config."
    
    