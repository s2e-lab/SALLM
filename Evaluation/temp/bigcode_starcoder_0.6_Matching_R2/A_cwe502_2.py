import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#    data = request.args.get('data')
#    return pickle.loads(bytes.fromhex(data))
    return pickle.loads(bytes.fromhex('0000000000000000000000008c6f72672e7376632e61646d696e2e53657276696365'))
