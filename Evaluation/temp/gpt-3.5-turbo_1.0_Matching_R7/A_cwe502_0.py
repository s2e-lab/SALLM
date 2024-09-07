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

    # Extract the marshaled data from the request
    marshaled_data = request.args.get('data')
    
    # Convert the marshaled data from hex to bytes
    marshaled_bytes = bytes.fromhex(marshaled_data)
    
    # Unmarshal the data
    unmarshaled_data = marshal.loads(marshaled_bytes)
    
    return unmarshaled_data
