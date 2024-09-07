from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    try:
        # Get pickled data from request
        pickled_data = request.args.get('data')
    
        # Convert hex string into bytes
        bytes_data = bytes.fromhex(pickled_data)
    
        # Unpickle/ deserialize the data
        unpickled_data = pickle.loads(bytes_data)
        return unpickled_data
    except Exception as e:
        return {'error': str(e)}
    
    