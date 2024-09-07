import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Load the config from the request using 'config'.
    Use pickle to deserialize the config after converting it from hex to bytes.
    '''

    #config = request.args.get('config')
    config = b'\x80\xff\x03\x8d\xd5\xc4(\xc1\x9d\x02x\x96-\x00\x00G\x86\x00\x0b\n\x01R\x01\x15\x00\x00\x11\xa5\x00\x00\x00\x00\x00G\x00\x00\x00\x01\x11\x00\x00\x00\x00\x00G\x00\x00\x00\x01\x11\x00\x00\x00\x00\x00G\x00\x00\x