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
        config_data = request.args.get('config')
        if config_data:
            config_data_bytes = bytes.fromhex(config_data)
            config = pickle.loads(config_data_bytes)
            return config
        else:
            return 'No config data provided', 400
    except Exception as e:
        return str(e), 500
    
    