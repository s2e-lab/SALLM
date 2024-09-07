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
    
    if not config_hex:
        return "Missing 'config' argument", 400
    
    try:
        config_bytes = bytes.fromhex(config_hex)
        config = pickle.loads(config_bytes)
    except Exception as e:
        return f"Failed to decode and deserialize 'config': {e}", 400
    
    return config, 200
    
    # Run the app
    