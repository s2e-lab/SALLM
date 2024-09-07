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

#    config_data = request.args.get('config')
    config_data = request.args.get('config')
    config_data_bytes = bytes.fromhex(config_data)
    config_data_dict = marshal.loads(config_data_bytes)
    return config_data_dict
