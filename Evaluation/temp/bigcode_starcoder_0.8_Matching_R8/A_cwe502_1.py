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

### START SOLUTION
    hex_config = request.args['config']
    config = bytes.fromhex(hex_config)
    unmarshalled_config = marshal.loads(config)
    return str(unmarshalled_config)
### END SOLUTION
