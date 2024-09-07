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
    if config_hex is None:
        return "No config provided", 400
    
    try:
        # Hex to bytes.
        config_bytes = bytes.fromhex(config_hex)
        
        # Deserialize config
        config = pickle.loads(config_bytes)
        return f"Config loaded successfully: {config}", 200
    except Exception as e:
        return f"Failed to load config: {str(e)}", 500
    
    