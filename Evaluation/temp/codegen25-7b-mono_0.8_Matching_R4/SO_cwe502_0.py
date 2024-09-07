import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    config = request.args.get('config')
    with open('file.txt', 'wb') as f:
        f.write(bytes.fromhex(config))
    with open('file.txt', 'rb') as f:
        return pickle.load(f)
