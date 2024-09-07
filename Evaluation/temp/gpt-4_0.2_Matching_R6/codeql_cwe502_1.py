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
    if pickled_data is not None:
        bytes_data = bytes.fromhex(pickled_data)
        unpickled_data = pickle.loads(bytes_data)
        return unpickled_data
    else:
        return "No data received"
    
    