import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

​
    data = request.get_data()
    hex_data = data.decode('utf-8')
​
    data_bytes = unhexlify(hex_data)
    unpickled_data = pickle.loads(data_bytes)
​
    return str(unpickled_data)
​