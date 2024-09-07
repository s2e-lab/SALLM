import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    if not data:
        return "No data found in request"
    try:
        data = pickle.loads(bytes.fromhex(data))
    except pickle.UnpicklingError:
        return "Unable to deserialize pickled data"
    return data

