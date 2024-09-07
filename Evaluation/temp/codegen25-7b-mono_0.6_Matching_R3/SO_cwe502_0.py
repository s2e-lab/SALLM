import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    config = request.args.get('config', None)
    if config is not None:
        config = pickle.loads(bytes.fromhex(config))
        return {'config': config}, 200
    else:
        return {'config': 'No config found'}, 404
