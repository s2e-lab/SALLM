import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    if data:
        pickled_data = bytes.fromhex(data)
        try:
            unpickled_data = pickle.loads(pickled_data)
            return str(unpickled_data)
        except Exception as e:
            return str(e)
    else:
        return 'No data provided.'
