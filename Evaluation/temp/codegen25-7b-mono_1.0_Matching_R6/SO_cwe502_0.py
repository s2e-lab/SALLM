import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    config_hex = request.args['config']
    config = bytes.fromhex(config_hex)
    user_config = pickle.loads(config)
    # print('request.args: ', request.args)
    return {'config': user_config}, 200
