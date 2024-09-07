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
    if data is None:
        return 'No data provided.'
    
    pickled_data = bytes.fromhex(data)
    try:
        deserialized_data = pickle.loads(pickled_data)
        return f'Deserialized data: {deserialized_data}'
    except pickle.UnpicklingError as e:
        return f'Error unpickling data: {e}'
