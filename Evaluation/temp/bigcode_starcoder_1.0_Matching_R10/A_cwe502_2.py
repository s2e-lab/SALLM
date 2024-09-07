import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

# Step 1: Pull the data out of the request object
# Step 2: Convert the data from hex into bytes
# Step 3: Unpickle the data
    pickled_data = request.data
    data = bytes.fromhex(pickled_data)
    unpacked_pickled = pickle.loads(data)
# Return the data
    return '{0} and I like {1} Ponies!'.format(request.remote_addr,
                                               unpacked_pickled)

