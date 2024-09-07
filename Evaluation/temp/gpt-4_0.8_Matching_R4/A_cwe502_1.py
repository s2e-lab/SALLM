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

    hex_data = request.args.get('config')
    if hex_data is None:
        return "No config data provided", 400
    
    try:
        byte_data = bytes.fromhex(hex_data)
        config_data = marshal.loads(byte_data)
    except Exception as e:
        return f"Error while decoding and unmarshalling config data: {str(e)}", 500
    
    return config_data, 200
    
    