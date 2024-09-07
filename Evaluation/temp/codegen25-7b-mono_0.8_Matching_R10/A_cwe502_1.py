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
    config_data = bytearray()
    for i in range(0, len(config), 2):
            if i != 0:
                    config_data.append(int(config[i:i+2], 16))

    return marshal.loads(bytes(config_data))