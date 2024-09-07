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
        return "No data provided", 400
    try:
        bytes_data = bytes.fromhex(data)
        unpickled_data = pickle.loads(bytes_data)
        return str(unpickled_data)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
    
    