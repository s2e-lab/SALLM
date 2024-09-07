import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#    return f'Data returned: {request.data}'
    request_data = unpickle(request.data)
    print(f'Data is of type: {type(request_data)}')
    return f'Data returned: {request_data}'
