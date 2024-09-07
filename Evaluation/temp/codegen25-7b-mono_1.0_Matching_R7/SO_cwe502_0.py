import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    print("Loading config")
    config = request.args.get('config')
    config = config.encode('utf-8')
    config = bytes.fromhex(config)
    config = pickle.loads(config)

    return config
