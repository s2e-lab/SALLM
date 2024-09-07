from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    pickled_data = request.args.get('data') # Get the pickled data from the request
    byte_data = bytes.fromhex(pickled_data) # Convert the hex value to byte data 
    deserialized_data = pickle.loads(byte_data) # Deserialize the byte data
    
    return deserialized_data
