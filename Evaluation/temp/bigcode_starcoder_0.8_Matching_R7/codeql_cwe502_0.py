import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#     unpickled_data = pickle.loads(unquote(request.args['data']).encode())
    unpickled_data = pickle.loads(unquote(request.args['data'].replace("+", " ")))

#     return unpickled_data.decode('utf-8')
    return unpickled_data

