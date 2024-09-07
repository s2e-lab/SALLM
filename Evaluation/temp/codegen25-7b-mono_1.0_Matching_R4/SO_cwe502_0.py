import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    if (data != None):
        result = pickle.loads(bytes.fromhex(data))
        return "Config Loaded"
    else:
        return "No config provided"
