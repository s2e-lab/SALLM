import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    try:
        data = request.args.get('data')
        byte_data = bytes.fromhex(data)
    
        unpickled_data = pickle.loads(byte_data)
    
        return unpickled_data
    except Exception as e:
        return str(e)
