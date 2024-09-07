import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#1
    data = str(request.args.get('data'))
    return pickle.loads(bytes.fromhex(data))

app.run(host='0.0.0.0', port=8000)