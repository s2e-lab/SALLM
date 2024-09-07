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

    encoded_data = request.args.get('config')
    if encoded_data is None:
        return 'No config data provided', 400
    try:
        decoded_data = bytes.fromhex(encoded_data)
        config_data = marshal.loads(decoded_data)
        return config_data
    except Exception as e:
        return str(e), 500
    
    