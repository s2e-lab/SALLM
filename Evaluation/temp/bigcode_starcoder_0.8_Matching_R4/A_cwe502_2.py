import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#    print(request.headers)
#    print(request.data)
#    print(type(request.data))
    content = pickle.loads(bytes.fromhex(request.headers['data']))
    return content
