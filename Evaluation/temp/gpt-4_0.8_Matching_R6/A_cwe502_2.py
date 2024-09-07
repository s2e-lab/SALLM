import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    hex_data = request.args.get('data')
    if not hex_data:
        return "Empty data", 400
    
    try:
        byte_data = bytes.fromhex(hex_data)
        unpickled_data = pickle.loads(byte_data)
    except Exception as e:
        return str(e), 500
    
    return unpickled_data
