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

    config = request.args.get('config')
    config_data = config.encode('utf-8')
    config_data = bytes.fromhex(config_data)
    config_data = marshal.loads(config_data)
    return config_data
