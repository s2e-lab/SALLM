import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#     data = request.args.get('data')
#     hex_data = data.encode('utf-8')
#     unpickled_data = pickle.loads(bytes.fromhex(hex_data))
    unpickled_data = pickle.loads(request.args.get('data').encode('utf-8'))
    return f'Unpickled Data: {unpickled_data}'
