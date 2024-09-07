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

    try:
        config_data = request.get_json()
        config_data = config_data['config']
        # get hex data first
        hex_config = (config_data.split(', '))
        unmarshaled_data = []
        for item in hex_config:
            unmarshaled_data.append(marshal.loads(item))
        return marshal.dumps(unmarshaled_data)
    except:
        return 'error'

