import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data_hex = request.args.get('data')
    data_bytes = bytes.fromhex(data_hex)
    data = pickle.loads(data_bytes)
    return data
