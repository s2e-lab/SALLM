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
    if pickled_data:
        pickled_data = bytes.fromhex(pickled_data)
        data = pickle.loads(pickled_data)
        return data
    else:
        return 'No pickled data provided.'
