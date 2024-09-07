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
    data = bytes.fromhex(data)
    unpickled_data = pickle.loads(data)
    return unpickled_data
    
    
    