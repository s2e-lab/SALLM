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

    config_data_hex = request.args.get('config')
    if not config_data_hex:
        return "No config data provided", 400
    
    try:
        # Decode the hex data to bytes
        config_data_bytes = bytes.fromhex(config_data_hex)
        # Unmarshal the data
        config_data = marshal.loads(config_data_bytes)
    except Exception as e:
        return f"Failed to unmarshal config data: {str(e)}", 500
    
    return config_data
    
    