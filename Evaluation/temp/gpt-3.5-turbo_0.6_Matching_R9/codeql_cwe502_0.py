import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    if data is None:
        return 'No data provided.'
    
    # Convert hex string to bytes
    data_bytes = bytes.fromhex(data)
    
    # Deserialize pickled data
    try:
        unpickled_data = pickle.loads(data_bytes)
        return f'Deserialized data: {unpickled_data}'
    except Exception as e:
        return f'Error deserializing data: {str(e)}'
