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

#     return str(request.args.get('config'))
    decoded_hex = request.args.get('config')
    decoded_data = decoded_hex.decode('hex')
    return str(marshal.loads(decoded_data))
