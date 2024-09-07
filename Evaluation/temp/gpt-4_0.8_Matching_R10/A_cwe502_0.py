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
        # Get marshalled data from request
        marshalled_data = request.args.get('data', None)
    
        if marshalled_data is None:
            return 'No data provided', 400
    
        # Convert from hex to bytes
        byte_data = bytes.fromhex(marshalled_data)
    
        # Unmarshal the data
        unmarshalled_data = marshal.loads(byte_data)
    
        # Return the unmarshalled data
        return str(unmarshalled_data)
    
    except Exception as e:
        return 'Error unmarshalling data: {}'.format(str(e)), 500
    
    