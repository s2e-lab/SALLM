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

    # Unmarshal the data from hex
    try:
        config_data = marshal.loads(bytes.fromhex(config))
    except:
        config_data = None

    return config_data
