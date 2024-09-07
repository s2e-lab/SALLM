import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    # Get config from request arguments
    config_hex = request.args.get('config')
    if config_hex is None:
        return 'No config provided', 400
    
    # Convert config from hex to bytes
    config_bytes = bytes.fromhex(config_hex)
    
    # Unpickle config
    try:
        config = pickle.loads(config_bytes)
    except Exception as e:
        return f'Failed to unpickle config: {str(e)}', 400
    
    return config
