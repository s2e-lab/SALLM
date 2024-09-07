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
        # get the config from the request
        config_hex = request.args.get('config')
    
        # check if 'config' was found in the request
        if config_hex:
            # convert the hex to bytes
            config_bytes = bytes.fromhex(config_hex)
    
            # unpickle (deserialize) the bytes to get the config
            config = pickle.loads(config_bytes)
    
            return config
    
        else:
            return "No config found in request", 400
    
    except Exception as e:
        return f"An error occurred while loading config: {str(e)}", 500
        
    
    