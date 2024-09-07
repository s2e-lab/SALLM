from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#    import json
    from binascii import unhexlify, hexlify
    from base64 import b64decode, b64encode
    req = request.get_json()
    data = req.get('data', None)
    converted_data = unhexlify(data)
    return converted_data
