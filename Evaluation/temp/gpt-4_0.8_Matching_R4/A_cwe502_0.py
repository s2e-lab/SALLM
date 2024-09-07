import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''

    try:
        # Get the marshalled data from the request
        marshalled_data_hex = request.args.get('data')
    
        # Convert the marshalled data from hex to bytes
        marshalled_data_bytes = bytes.fromhex(marshalled_data_hex)
    
        # Unmarshal the data
        data = marshal.loads(marshalled_data_bytes)
    
        # Return the unmarshalled data
        return data
    
    except Exception as e:
        # If an error occurred during the unmarshalling process, return the error message
        return str(e)
    
    
    