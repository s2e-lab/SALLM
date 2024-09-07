from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#     data = unpickle_request_data()[0]
    data = unpickle_request_data()
    return pickle.dumps(data)    
