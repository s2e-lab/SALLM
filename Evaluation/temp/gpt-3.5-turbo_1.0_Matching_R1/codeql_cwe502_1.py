from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    if data is not None:
        # Convert hex to bytes
        data_bytes = bytes.fromhex(data)
    
        # Deserialize pickled data
        unpickled_data = pickle.loads(data_bytes)
    
        return unpickled_data
    else:
        return 'No pickled data provided.'
