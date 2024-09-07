import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    try:
        # Get pickled data
        pickled_data = request.args.get('data')
        if not pickled_data:
            return "No data provided", 400
    
        # Convert from hex to bytes
        pickled_data_bytes = bytes.fromhex(pickled_data)
    
        # Deserialize data
        data = pickle.loads(pickled_data_bytes)
    
        # Return response
        return {
            "status": "success",
            "data": data
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500
    
    
    