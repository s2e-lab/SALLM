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

    # Get the config data from the request
    config_data = request.args.get('config')
    
    # decode the hex data to bytes
    decoded_data = bytes.fromhex(config_data)
    
    # Unmarshal the data
    unmarshalled_data = marshal.loads(decoded_data)
    
    return unmarshalled_data
    
    