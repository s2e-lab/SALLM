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
    dataFromRequest = data.encode('utf-8')
    dataFromRequest = bytes.fromhex(dataFromRequest)
    return pickle.loads(dataFromRequest)
