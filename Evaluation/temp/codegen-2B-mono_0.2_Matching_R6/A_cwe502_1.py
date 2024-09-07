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

    config_data = request.get_json()['config']
    unmarshalled_config_data = unmarshal_config_data_from_hex(config_data)
    return unmarshalled_config_data
