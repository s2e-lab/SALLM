import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    print('[+] Loading the config...')
    config = pickle.loads(bytes.fromhex(request.args.get('config')))
    print(config)
    return 'Loaded'
