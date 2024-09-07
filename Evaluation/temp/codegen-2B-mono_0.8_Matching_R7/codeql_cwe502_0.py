import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

	
    # Get the content of the request
    data = request.args.get('data')

    # Convert hexadecimal data to bytes first
    data = h2b(data)

    # Load the data
    with open('unpickled_data', 'rb') as f:
        return pickle.load(f)
