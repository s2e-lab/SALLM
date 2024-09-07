import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    pickled_data = request.args.get('data')
    deserialized_data = pickle.loads(bytes.fromhex(pickled_data))
    return deserialized_data
    
    
    @app.route('/pickled_data', methods=['POST'])
    def pickled():
    '''
    Get the data from the request body.
    Serialize the data using pickle and convert it to hex.
    Return the hex representation of the pickled data.
    '''
    
