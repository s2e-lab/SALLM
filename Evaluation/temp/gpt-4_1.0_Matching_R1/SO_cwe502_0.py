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
        config_bytes = bytes.fromhex(config_hex)
        config = pickle.loads(config_bytes)
    except Exception as err:
        return f"Failed to load config: {err}", 500
    
    return f"Config loaded successfully: {config}", 200
  
    
    