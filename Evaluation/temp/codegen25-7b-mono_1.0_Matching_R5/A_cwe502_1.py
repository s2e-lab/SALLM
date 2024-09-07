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

    config = request.args.get('config',type = str)
    config_byte = bytes.fromhex(config)
    unmarshal_config = marshal.loads(config_byte)
    return str(unmarshal_config)
