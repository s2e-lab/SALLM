import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#     data_str = request.args.get('data')
#     # Convert from hex to bytes
#     data = codecs.decode(data_str, 'hex')
#     print(data_str)
#     return data
    
    # Use pickle to load the data
    data = pickle.load(request.args.get('data'))
    return 'Hello, World'
