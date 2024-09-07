import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    try:
        config_hex = request.args.get('config')
        if not config_hex:
            return 'Error: Missing "config", please provide a valid config.', 400
    
        # From hex to bytes
        config_bytes = bytes.fromhex(config_hex)
        
        # Deserializing
        config = pickle.loads(config_bytes)
    
        return f'Config loaded successfully: {config}', 200
    
    except Exception as e:
        return f"Error: {str(e)}", 500
    
    