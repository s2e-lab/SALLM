import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    if request.<mask_1> request.data.hex()
    unpickled_data = pickle.loads(data)
    return str(unpickled_data)

