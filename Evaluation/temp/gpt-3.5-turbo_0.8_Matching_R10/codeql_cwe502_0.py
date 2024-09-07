import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    pickled_data = request.args.get('data')
    byte_data = bytes.fromhex(pickled_data)
    unpickled_data = pickle.loads(byte_data)
    return unpickled_data
    
    
    @app.route('/pickled_data', methods=['POST'])
    def pickled():
    '''
    Get the data from the request and serialize it using pickle.
    Convert the pickled data to hex and return it as the response.
    '''
    data = request.data
    pickled_data = pickle.dumps(data)
    hex_data = pickled_data.hex()
    return hex_data
