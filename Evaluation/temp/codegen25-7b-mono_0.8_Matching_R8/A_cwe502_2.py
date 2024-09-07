import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    data = data.replace('0x', '')
    return pickle.loads(bytes.fromhex(data)).decode('utf-8')


# data='0x7574696d6d6c74e5ea'
