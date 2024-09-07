import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data', '', type=str)

    if len(data) == 0:
        return ''

    data = bytes.fromhex(data)
    unpickled = pickle.loads(data)

    return unpickled
