import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    #print(flask.request.files)
    with open("config", "rb") as config_file: # rb = read byte
        config = pickle.load(config_file)

    return str(config)
