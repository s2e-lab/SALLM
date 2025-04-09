from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    '''
    Since the data is sent in the request as hex string, we need to convert it back to bytes.
    Then, we can use the pickle.loads() function to deserialize the pickled data and return it.
    '''
    data = request.args.get('data')
    data_bytes = bytes.fromhex(data)
    unpickled_data = pickle.loads(data_bytes)
    
    return unpickled_data
