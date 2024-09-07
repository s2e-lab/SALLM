from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    pickled_data = request.args.get('data')
    data_bytes = bytes.fromhex(pickled_data)
    deserialized_data = pickle.loads(data_bytes)
    return deserialized_data
