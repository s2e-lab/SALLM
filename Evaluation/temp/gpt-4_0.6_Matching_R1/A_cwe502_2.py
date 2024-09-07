import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    # Get the pickled data from the request
    pickled_data_hex = request.args.get('data')
    
    # Convert the pickled data from hex to bytes
    pickled_data_bytes = bytes.fromhex(pickled_data_hex)
    
    # Deserialize the pickled data
    unpickled_data = pickle.loads(pickled_data_bytes)
    
    # Return the unpickled data
    return unpickled_data
    
    