from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    pickled_data = request.args.get('data', None)
    if pickled_data is None:
        return "No data received"
    else:
        try:
            # converting the hex to bytes
            byte_data = bytes.fromhex(pickled_data)
    
            # unpickling the byte data
            unpickled_data = pickle.loads(byte_data)
    
            return str(unpickled_data)
        except Exception as e:
            return "An error occurred: " + str(e)
    
    