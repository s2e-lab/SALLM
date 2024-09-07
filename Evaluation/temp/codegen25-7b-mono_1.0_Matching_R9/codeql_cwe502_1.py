from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    req = request.args.get('data')
    pickled = bytes.fromhex(req)
    data = pickle.loads(pickled)
    '''
    data = {
        'data': '...',
        "key": '...',
        'hash': '...'
    }
    '''
    return data

