import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''


#     # Get data for decoding.
#     data = request.args.get("data")

#     # Convert hex to bytes.
#     byte_data = unhexlify(data)

#     # Unpickle the data.
#     unpickled = pickle.loads(byte_data)

#     # Return JSON response.
#     return jsonify(unpickled)

    # Get data.
    data = request.args.get("data")

    # Return JSON response.
    return jsonify(data)

