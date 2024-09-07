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

#    config_data = request.get_data('config')
    config_data = request.args.get('config')
    decoded_config = config_data.decode('hex')
    decoded_config = ast.literal_eval(decoded_config)
    return str(decoded_config) 
