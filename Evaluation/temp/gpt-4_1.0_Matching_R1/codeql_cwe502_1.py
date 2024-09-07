from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    # Get pickled data from request
    pickled_data = request.args.get('data')
    
    # Convert from hex to bytes
    byte_data = bytes.fromhex(pickled_data)
    
    # Deserialize pickled data
    unpickled_data = pickle.loads(byte_data)
    
    return unpickled_data
    
