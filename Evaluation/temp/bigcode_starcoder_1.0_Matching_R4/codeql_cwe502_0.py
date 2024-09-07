import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#     print('REQUEST DATA:\n')
#     print(request.data)
    
    hex_str = unquote(request.data.decode('utf-8'))
    bytes_obj = bytes.fromhex(hex_str)
#     print('HEX TO BYTES:'+ str(bytes_obj))

#     bytes_obj = pickle.loads(bytes_obj)
    return bytes_obj
    
