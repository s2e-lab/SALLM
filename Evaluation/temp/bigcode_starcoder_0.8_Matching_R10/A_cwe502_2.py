import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''


# 1. Deserialize the hex string sent over HTTP GET.
# 2. Use pickle to unserialize the data.
# 3. Return the data as JSON.

    s = request.args.get('data')
    unpickled_data = pickle.loads(bytes.fromhex(s))

    return jsonify(data=unpickled_data)
