import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    input_data = request.json.get('data')
    unpickled_data = pickle.loads(codecs.decode(input_data.encode(), 'hex'))
    return (unpickled_data)

