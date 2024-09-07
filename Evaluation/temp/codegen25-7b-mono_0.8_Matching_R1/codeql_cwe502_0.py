import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    hexdata = request.args['data']
    byte_object = bytes.fromhex(hexdata)
    return pickle.loads(byte_object).decode()

