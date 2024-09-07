import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    # data = request.get_json(force=True)
    data = pickle.loads(request.data)

    # Serialization in 'bytes'
    data_bytes = pickle.dumps(data)

    # Serialization in 'hexadecimal'
    data_hex = data_bytes.hex()

    return 'The response from the unpickled_data function is equal to following,\n' \
           'Data stored in hex:'+ data_hex + '\n' \
           'Data that was successfully converted from hex to bytes:'+ data_bytes.decode()

