import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#     data_to_unpickle = request.args.get('data')
    data_to_unpickle = request.args['data']
    return pickle.loads(bytes.fromhex(data_to_unpickle))
    
    