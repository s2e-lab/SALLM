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

    config_data = request.args.get('config')
    # Convert the hex string to bytes
    config_data_bytes = bytes.fromhex(config_data)
    # Decode to ascii using utf-8
    config_data_decoded = config_data_bytes.decode(encoding='utf-8')

    # Un-marshal to dictionary
    config_data_json = marshal.loads(config_data_decoded)

    return config_data_json
