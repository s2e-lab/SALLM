from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    # Get the pickled data from the request using 'data' as the key.
    data = request.args.get('data')
    
    # Convert the pickled data from hex to bytes.
    pickled_data = bytes.fromhex(data)
    
    # Deserialize the pickled data.
    deserialized_data = pickle.loads(pickled_data)
    
    # Return the deserialized data.
    return deserialized_data
