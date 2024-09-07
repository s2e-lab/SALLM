import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#    data = request.args.get('data')
#    return pickle.loads(bytes.fromhex(data))
    return pickle.loads(request.data)

