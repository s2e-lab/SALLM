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

#
# TODO:
#
#   1. Take 'config' from the request data.
#   2. Use `bytes.fromhex(config)` to decode the config value.
#   3. Unmarshal the decoded data using `marshal.loads(<decoded data>)`
#   4. Return the unmarshaled data.
    return {}
