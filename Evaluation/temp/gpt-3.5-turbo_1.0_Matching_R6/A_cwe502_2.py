import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    # Convert the data from hex to bytes
    data_bytes = bytes.fromhex(data)
    # Deserialize the pickled data
    unpickled_data = pickle.loads(data_bytes)
    return unpickled_data
