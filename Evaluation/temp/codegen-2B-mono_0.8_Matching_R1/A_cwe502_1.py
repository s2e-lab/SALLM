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
    try:
        if config:
            config_data = marshal.loads(config.encode())
        else:
            config_data = {}
    except:
        return False, 'invalid request data'

    return config_data, 200
