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
    if data is None:
        return "Data key not found"
    with open('cache', 'rb') as f:
        data_cache = pickle.load(f)
    with open('cache_hex', 'wb') as f:
        pickle.dump(data_cache, f)
    with open('cache_hex', 'rb') as f:
        data_cache = pickle.load(f)
    unpickled_data = deserialize(data_cache)
    return unpickled_data



