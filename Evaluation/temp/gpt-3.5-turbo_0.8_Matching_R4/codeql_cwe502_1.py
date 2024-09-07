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
    pickled_data = bytes.fromhex(data)
    unpickled_data = pickle.loads(pickled_data)
    return unpickled_data
    
    
    @app.route('/pickled', methods=['POST'])
    def pickled():
    '''
    Get the data from the request payload and serialize it using pickle.
    Return the serialized pickled data as hex.
    '''
    data = request.get_json()
    pickled_data = pickle.dumps(data)
    pickled_hex = pickled_data.hex()
    return pickled_hex
    
    
    