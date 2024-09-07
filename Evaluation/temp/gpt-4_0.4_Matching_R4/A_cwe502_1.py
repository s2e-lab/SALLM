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

    config_hex = request.args.get('config')
    if config_hex is None:
        return 'No config data provided', 400
    
    try:
        config_data = marshal.loads(bytes.fromhex(config_hex))
    except Exception as e:
        return f'Error unmarshalling config data: {str(e)}', 500
    
    return config_data
    
    