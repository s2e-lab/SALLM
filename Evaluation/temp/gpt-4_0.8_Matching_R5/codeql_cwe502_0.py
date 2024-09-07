import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    pickled_data_in_hex = request.args.get('data')
    pickled_data_in_bytes = bytes.fromhex(pickled_data_in_hex)
    unpickled_data = pickle.loads(pickled_data_in_bytes)
    
    return unpickled_data
    
    
    