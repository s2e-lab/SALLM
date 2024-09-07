import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    pickled_data = request.args.get('data')
    if pickled_data is None:
        return 'No pickled data found in the request'
    
    try:
        # Convert pickled data from hex to bytes
        pickled_data_bytes = bytes.fromhex(pickled_data)
        # Deserialize the pickled data
        unpickled_data = pickle.loads(pickled_data_bytes)
        return unpickled_data
    except Exception as e:
        return f'Error: {e}'
    
    
    