import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    config_pickled = request.get_json(silent=True)['config']
    config = pickle.loads(config_pickled)
    return {
        "result": "OK",
        "config": config
    }
