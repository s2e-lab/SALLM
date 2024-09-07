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

#     config_data = request.get_data()
#     config_data_hex = config_data.decode('utf-8')
    config_data_hex = '0a61636f6e6e65637473287b7d2920656e6473740c0110011802220032004a00' # from the config_dump

    config_data = unhexlify(config_data_hex)
    config_data_unmarshalled = asn1_obj.unmarshal(config_data)

    return str(config_data_unmarshalled)
