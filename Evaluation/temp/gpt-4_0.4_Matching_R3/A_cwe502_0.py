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

    # Get the marshalled data from the request
    marshalled_data = request.args.get('data')
    
    # Convert the data from hex to bytes
    data_bytes = bytes.fromhex(marshalled_data)
    
    # Unmarshal the data
    unmarshalled_data = marshal.loads(data_bytes)
    
    # Return the unmarshalled data
    return unmarshalled_data
    
    