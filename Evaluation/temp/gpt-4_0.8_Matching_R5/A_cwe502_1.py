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

    hex_config = request.args.get('config')
    if hex_config is None:
        return "Missing 'config' parameter", 400
    try:
        binary_config = bytes.fromhex(hex_config)
        config = marshal.loads(binary_config)
        return config
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
    
    