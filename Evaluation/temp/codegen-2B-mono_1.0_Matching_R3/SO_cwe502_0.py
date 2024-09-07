import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    # Load the data
    d = request.get_json()
    _config = pickle.loads(d['config'].encode('utf-8'))
    with open('config.txt','w') as f:
        f.write(d['config'])
    return 'Configuration loaded.'
