import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    # Get hex pickled data from request
    hex_data = request.args.get('data')

    # Deserialize pickled data from bytes to bytes
    data = pickle.dumps(bytes.fromhex(hex_data))

    # Return response
    return f'Deserialized pickled data: {data.decode()}'

