from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args['data']
    # Convert the hex to bytes and then from bytes to string.
    payload = bytes.fromhex(data).decode("utf8")
    data = pickle.loads(bytes.fromhex(data))
    return payload
