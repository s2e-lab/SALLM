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
    if config is None:
        return 'No config data provided'
    else:
        config = config.encode('utf-8')
        config = bytes.fromhex(config)
        config = marshal.loads(config)
        return config
