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

    # Get the raw config data from the request
    config_data = request.get_data()
    # Decode the config data from hex to a string
    config_data = config_data.decode('hex')
    # Unmarshal the config data
    unmarshalled_config_data = unmarshal_config_data_from_string(config_data)
    # Return the unmarshalled data
    return unmarshalled_config_data
