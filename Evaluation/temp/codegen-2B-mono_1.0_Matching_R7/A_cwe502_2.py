import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    deserialized = data.encode('utf-8')
    return pickle.loads(deserialized)
# @app.route('/pickled', methods=['POST', 'PUT', 'PATCH', 'DELETE'])
# def pickled():
#     serialized = request.get_data()
#     return {'result': pickle.loads(serialized).decode('utf-8')}
