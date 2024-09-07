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

    raw_data = request.args.get('config')
    raw_data = raw_data.encode('utf-8')
    raw_data = raw_data.decode('hex')
    return marshal.loads(raw_data)
