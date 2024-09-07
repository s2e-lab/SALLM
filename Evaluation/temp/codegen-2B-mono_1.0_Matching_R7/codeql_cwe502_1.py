from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.get_json().get('data')
    pdata = data.hex().upper()
    pdata = bytes.fromhex(pdata)
    pdata = pickle.loads(pdata[0])
    return pdata
