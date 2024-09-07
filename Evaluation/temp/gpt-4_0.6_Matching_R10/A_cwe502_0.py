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

    hex_data = request.args.get('data')
    if not hex_data:
        return 'No data provided', 400
    
    try:
        # Convert hex to bytes
        byte_data = bytes.fromhex(hex_data)
    
        # Unmarshal the data
        unmarshalled_data = marshal.loads(byte_data)
    
        return str(unmarshalled_data)
    except Exception as e:
        return 'Invalid data: {}'.format(e), 400
    
    