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
    if pickled_data is None:
        return 'No pickled data found in the request.'
    
    try:
        # Convert pickled data from hex to bytes
        pickled_bytes = bytes.fromhex(pickled_data)
        # Deserialize the pickled data
        deserialized_data = pickle.loads(pickled_bytes)
        return f'Deserialized data: {deserialized_data}'
    except Exception as e:
        return f'Error: {e}'
