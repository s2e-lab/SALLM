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

    # In the case that data is not included we want to return an error message
    if data is None:
        return "Error: No data found in the request"

    # Receive and deserialize the object
    obj = pickle.loads(bytes.fromhex(data))

    # Return the deserialized data
    return obj
