import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    # Request the config from the user
    config_hex = request.args.get('config', b'').decode('ascii')
    print(config_hex)
    # Check if there is a config in the request or return an error
    if config_hex == '':
        return 'No config was provided.'

    # Deserialize the configs from hex to bytes
    config = pickle.loads(bytes.fromhex(config_hex))
    print(type(config))
    return config

