from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#    data = request.args.get('data')
    data = request.args.get('data')

    # Deserialize the data and convert it from hex to bytes.
    data = pickle.loads(bytes.fromhex(data))

    return "You sent me this: " + data
