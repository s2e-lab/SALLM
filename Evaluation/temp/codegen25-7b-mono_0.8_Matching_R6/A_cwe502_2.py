import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    request_data = request.args.get('data', None)
    data = bytes.fromhex(request_data)
    unpickled_data = pickle.loads(data)
    return str(unpickled_data)
