import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    req = request.get_json()
    data = req['data']
    return pickle.loads(data.encode('utf-8')).hex()

