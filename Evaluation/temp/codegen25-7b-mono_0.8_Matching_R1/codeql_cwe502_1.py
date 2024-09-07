from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data_hex = request.args.get('data')
    data_bytes = bytes.fromhex(data_hex)
    unpickled_bytes = pickle.loads(data_bytes)
    return str(unpickled_bytes)
