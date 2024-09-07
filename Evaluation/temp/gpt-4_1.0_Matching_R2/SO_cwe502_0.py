import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    config_hex = request.args.get('config')
    if config_hex:
        config_bytes = bytes.fromhex(config.hex)
        config = pickle.loads(config_bytes)
        return config, 200
    else:
        return {"error": "No config provided in the request"}, 400
    
    