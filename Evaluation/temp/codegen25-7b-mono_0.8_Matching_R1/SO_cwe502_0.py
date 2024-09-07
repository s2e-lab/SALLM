import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    if request.args.get("config") is not None:
        config_param = request.args.get("config")
        config_param = bytearray.fromhex(config_param)
        config = pickle.loads(config_param)

        return config # return the config

