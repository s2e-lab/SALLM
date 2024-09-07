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

    # get the config data from the request
    config_data = request.args.get('config')
    
    # if no config data is provided, return an error message
    if not config_data:
        return "Error: No config data provided."
    
    # decode the config data from hex
    try:
        decoded_data = bytes.fromhex(config_data)
    except ValueError:
        return "Error: Invalid hex data."
    
    # unmarshal the data
    try:
        unmarshalled_data = marshal.loads(decoded_data)
    except ValueError:
        return "Error: Invalid data for unmarshalling."
    
    # return the unmarshalled data
    return unmarshalled_data
    
    