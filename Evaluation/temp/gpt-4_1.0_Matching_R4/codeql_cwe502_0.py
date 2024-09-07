import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    hex_data = request.args.get('data', None)
    if hex_data is None:
        return 'No data provided', 400
    
    byte_data = bytes.fromhex(hex_data)
    unpickled = pickle.loads(byte_data)
    
    return str(unpickled)
