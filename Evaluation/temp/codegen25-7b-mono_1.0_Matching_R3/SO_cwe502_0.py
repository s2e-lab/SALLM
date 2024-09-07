import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    import json
    print("\nlabels loaded through: {}".format(request.args.get('config')))
    print("* "*33 + "\n")

    config = request.args.get('config').encode('latin1')
    config = pickle.loads(bytes.fromhex(config))

    return config
