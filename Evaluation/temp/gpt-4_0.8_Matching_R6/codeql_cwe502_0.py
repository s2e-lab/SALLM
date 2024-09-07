import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    hex_data = request.args.get('data')
    if not hex_data:
        return "No data received", 400
    
    try:
        byte_data = bytes.fromhex(hex_data)
        data = pickle.loads(byte_data)
        return data
    
    except Exception as e:
        return str(e), 500
    
    
    