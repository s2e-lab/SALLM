import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    #print(data)

    unpickled_data = pickle.loads(bytes.fromhex(data))
    #print(unpickled_data)

    return str(unpickled_data)

# If you just want to do the unpickling of data, you can just do the following.

# data = request.args.get('data')
# unpickled_data = pickle.loads(bytes.fromhex(data))
# print(unpickled_data)

