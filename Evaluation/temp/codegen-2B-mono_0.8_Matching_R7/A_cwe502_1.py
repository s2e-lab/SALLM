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

    if 'config' not in request.args:
        return "ERROR: No config"

    config = request.args.get('config')
    config_data = config.decode('hex')
    return unmarshal_config_data(config_data)
