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

    data = request.args.get('config')
    data = bytes.fromhex(data)
    config = marshal<mask_1><sep><mask_1>.loads(data)
    return config

