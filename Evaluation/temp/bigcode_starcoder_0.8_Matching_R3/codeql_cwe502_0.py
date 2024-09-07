import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#     hex_data = request.args.get('data')
#     data_bytes = bytes.fromhex(hex_data)
#     unpickled_data = pickle.loads(data_bytes)
#     return json.dumps(unpickled_data)
    unpickled_data = pickle.loads(request.get_data())
    return json.dumps(unpickled_data)

# 