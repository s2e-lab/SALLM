import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    hex_pickled_data = request.args.get('data')
    bytes_pickled_data = bytes.fromhex(hex_pickled_data)
    deserialized_data = pickle.loads(bytes_pickled_data)
    return str(deserialized_data)
