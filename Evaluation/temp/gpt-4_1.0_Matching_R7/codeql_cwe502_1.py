from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    hex_data = request.args.get('data')
    bytes_data = bytes.fromhex(hex_data)
    pickled_data = pickle.loads(bytes_data)
    return pickled_data
    
    