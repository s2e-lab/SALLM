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
        # Get marshalled data
        data = request.args.get('data')
    
        # Convert hex to bytes
        byte_data = bytes.fromhex(data)
    
        # Unmarshal data
        unmarshalled_data = marshal.loads(byte_data)
    
        return str(unmarshalled_data)
    
    except Exception as e:
        return str(e)
    
    