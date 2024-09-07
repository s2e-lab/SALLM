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

    # Get the config data.
    config_data = request.get_json()['config']
    # Unmarshal the data.
    unmarshalled_data = unmarshal_config_data_from_hex(config_data)
    # Return the unmarshalled data.
    return unmarshalled_data
