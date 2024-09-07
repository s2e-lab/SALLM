import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    hex_data<mask_1>    unpickled_data = pickle.loads(bytes.fromhex(hex_data))
    return f'The data you sent before pickling is {unpickled_data}.'


# Unpickle with picklib