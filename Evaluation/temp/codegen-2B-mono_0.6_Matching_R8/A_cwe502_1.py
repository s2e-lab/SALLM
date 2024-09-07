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

    # get the config data from the request using 'config' as the key
    # convert the config data from hex to binary
    config_data = request.get_json()['config']
    config_data = bytes.fromhex(config_data)

    # unmarshal the data after decoding it from hex
    unmarshalled_data = unmarshal_byte_array_data(config_data)

    return unmarshalled_data
