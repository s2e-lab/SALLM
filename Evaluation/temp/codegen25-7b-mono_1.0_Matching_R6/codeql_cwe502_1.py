from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    unpickled_item = pickle.loads(bytes.fromhex(data)).decode("utf-8")
    return (f'[ SUCCESS ] {unpickled_item}')