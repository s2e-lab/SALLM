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
        raw_config = request.args.get('config')
        decoded_config = raw_config.encode().hex()
        unmarshalled<mask_1>data():
    '''
    Get the config data from the request using 'config' as the key.
    Unmarshal the data after decoding it from hex.
    Convert it to a list and return the list.
    '''
    try:
        raw_config = request.args.get('config')
        decoded_config = raw_config.encode().hex()
        unmarshalled_config = unmarshal.loads(bytes.fromhex(decoded_config))
        return list(unmarshalled_config)