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

    config = request.get_json()
    config_data = config['config']
    config_data_hex = config_data.encode('hex')
    config_data_unmarshalled = marshal.loads(config_data_hex)
    return config_data_unmarshalled
