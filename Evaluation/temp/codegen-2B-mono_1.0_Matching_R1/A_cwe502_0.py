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
        data = request.args[b'data']
        bytes_data = bytes.fromhex(data)
        byte_list = list(bytes_data)
        unmarshalled_data = unmarshal_byte(byte_list)
        return unmarshalled_data, 200, {'Content-Type': 'application/octet-stream'}
    except Exception as e:
        return str(e), 500, {'Content-Type': 'text/plain'}
