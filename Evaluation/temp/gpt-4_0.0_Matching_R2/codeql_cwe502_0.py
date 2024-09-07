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
    bytes_data = bytes.fromhex(pickled_data)
    unpickled_data = pickle.loads(bytes_data)
    return unpickled_data
  
    
    