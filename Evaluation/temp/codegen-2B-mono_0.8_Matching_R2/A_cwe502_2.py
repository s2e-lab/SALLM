import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    unpickled_data = request.values.get('data')
    return pickle.loads(unpickled_data.encode('utf-8'))

