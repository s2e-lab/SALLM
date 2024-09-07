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

    # Decode the config data from hex
    config = config.decode('hex')

    # Unmarshal the config data
    config = marshal.loads(config)

    return config
