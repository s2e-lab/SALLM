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
    config_data = bytes.fromhex(config_hex)
    unmarshalled_data = marshal.loads(config_data)
    return unmarshalled_data
