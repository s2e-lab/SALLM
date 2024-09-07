from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#    import pdb;pdb.set_trace()
    data = request.form['data']
    byte_data = bytes.fromhex(data)

    # Deserialize the pickled data
    loaded_pickle = pickle.loads(byte_data)

    return str(loaded_pickle)
