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

    request_data = request.get_json()
    # Get the config from the request
    config_data = request_data['config']
    # Decode the config data
    config_data = bytes.fromhex(config_data).decode()
    # Return the data
    return config_data
