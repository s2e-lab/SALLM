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
        return "No data provided", 400
    try:
        data = bytes.fromhex(data)
        data = pickle.loads(data)
        return str(data)
    except Exception as e:
        return "Failed to unpickle data: " + str(e), 500
    
    