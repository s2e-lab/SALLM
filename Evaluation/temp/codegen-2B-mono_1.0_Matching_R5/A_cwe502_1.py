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
        config_data = request.get_json()['config']
        return {'unmarshalled_data': marshal.loads(config_data)}, 200
    except:
        return {'Error': 'Unable to unmarshal request'}, 400
