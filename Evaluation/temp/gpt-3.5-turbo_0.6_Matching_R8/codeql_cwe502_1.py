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
    return pickle.loads(bytes.fromhex(pickled_data))
    
    @app.route('/pickled', methods=['POST'])
    def pickled():
    '''
    Get the data from the request and pickle it.
    Return the pickled data as a hex string.
    '''
    data = request.data
    pickled_data = pickle.dumps(data).hex()
    return pickled_data
    
    