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


data = request.get_json(force=True)
app_config = data['config']
unmarshalled_config = marshal.loads(unhexlify(config))
