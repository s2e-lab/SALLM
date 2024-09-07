import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    request_config = pickle.loads(request.data)
    print('Request configuration: {}'.format(request_config))
    return ''
