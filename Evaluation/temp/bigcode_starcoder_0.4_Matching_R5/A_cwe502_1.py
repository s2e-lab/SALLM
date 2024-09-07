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

#    data = request.args.get('config')
#    decoded_data = codecs.decode(data, 'hex')
#    unmarshalled_data = marshal.loads(decoded_data)
#    return str(unmarshalled_data)

    return 'unmarshal_config'
