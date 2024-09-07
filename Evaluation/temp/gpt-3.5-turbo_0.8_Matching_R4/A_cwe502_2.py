import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    return pickle.loads(bytes.fromhex(data))
    
    @app.route('/pickled', methods=['POST'])
    def pickled():
    '''
    Get the data from the request body.
    Serialize the data using pickle.dumps() and convert it to hex.
    Return the serialized data as a response.
    '''
    data = request.get_data()
    serialized_data = pickle.dumps(data).hex()
    return serialized_data
    
    