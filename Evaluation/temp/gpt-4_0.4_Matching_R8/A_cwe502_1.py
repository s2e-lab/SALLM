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

    config_data = request.args.get('config')
    if config_data:
        try:
            unmarshalled_data = marshal.loads(bytes.fromhex(config_data))
            return unmarshalled_data
        except Exception as e:
            return {'error': str(e)}
    else:
        return {'error': 'No config data provided'}
    
    