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
    if hex_data is None:
        return "No data found in the request"
    
    byte_data = bytes.fromhex(hex_data)
    
    try:
        unmarshalled_data = marshal.loads(byte_data)
    except Exception as e:
        return str(e)
    
    return str(unmarshalled_data)
    
    