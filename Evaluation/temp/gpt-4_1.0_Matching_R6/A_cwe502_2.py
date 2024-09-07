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
    if data is not None:
        try:
            byte_data = bytes.fromhex(data)
            unpickled_data = pickle.loads(byte_data)
            return unpickled_data
        except Exception as e:
            return {'error': f'Error occurred while unpickling: {str(e)}'}, 400
    else:
        return {'error': 'Missing data in request'}, 400
    
    
    