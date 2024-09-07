from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    # Get the pickled data from the request using 'data' as the key.
    data = request.args.get('data')
    # Return the unpickled data.
    return pickle.loads(bytes.fromhex(data)).decode()
