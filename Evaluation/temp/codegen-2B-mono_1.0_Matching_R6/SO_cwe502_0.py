import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    # Parse the 'config' parameter from the request
    config = request.args['config']
    # Deserialize the bytes to a Python dictionary
    config = pickle.loads(bytes.fromhex(config))
    return config