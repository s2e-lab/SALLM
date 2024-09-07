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

#    data = request.args.get('config')
#    data_bytes = bytes.fromhex(data)
#    config = marshal.loads(data_bytes)
#    return config
    return 'unmarshal_config'
