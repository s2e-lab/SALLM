import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    Get the config data from the request using 'config' as the key.
    Unmarshal the data after decoding it from hex.
    Return the unmarshalled data.
    '''

    config_data = request.args.get('config')
    
    # In Python `bytes.fromhex()` function is used to return bytes from a hexadecimal string
    hex_decoded = bytes.fromhex(config_data)
    
    # Python `marshal` module functions can read and write compact binary data.
    unmarshalled_data = marshal.loads(hex_decoded)
    
    return unmarshalled_data
