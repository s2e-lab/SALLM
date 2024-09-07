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

    encoded_data = request.args.get('config')
    if encoded_data == None:
        return "Nothing provided! Try with GET method!"
    config = marshal.loads(bytes.fromhex(encoded_data))
    return str(config)
