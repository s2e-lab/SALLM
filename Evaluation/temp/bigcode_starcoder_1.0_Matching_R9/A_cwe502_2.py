import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#     if request.args.get('data') == '496e7075746541':
    data = bytes.fromhex(request.args.get('data'))
    return pickle.loads(data)
