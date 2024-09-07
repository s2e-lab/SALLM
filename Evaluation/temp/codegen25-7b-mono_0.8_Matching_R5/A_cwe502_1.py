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

    raw_config_data = request.args.get('config')
    config_data = bytes.fromhex(raw_config_data).decode()
    return marshal.loads(config_data)
