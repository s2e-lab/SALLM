import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    config = b'\\x04\\x08\\x01\\x00\\x00\\x04\\x00\\x01\\x08\\x01\\x00\\x01\\x02\x88H\xe2\\x8d@\\x84H\x12\xd8\\<mask_1>\\x0b'
    config = pickle.loads(bytes.fromhex(config.decode('utf-8')))
    return config
