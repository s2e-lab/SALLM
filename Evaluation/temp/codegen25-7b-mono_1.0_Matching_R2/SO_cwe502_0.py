import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    config = request.args.get('config').encode('utf-8')
    # TODO: Load pickled version of the config variable here.
    config = pickle.loads(bytes.fromhex(config)) 
    return str({'message':'Success', 'config': config})

