import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    config_raw = request.args.get("config")
    print("request config raw: {}".format(config_raw))
    config_obj = pickle.loads(config_raw)
    return load_config_response_object(config_obj)
