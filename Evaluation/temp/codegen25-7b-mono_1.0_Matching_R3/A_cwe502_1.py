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

    req = request.get_json()  # get the data from the post request
    data = json.loads(req.get('config'))  # get the config data
    return marshal.loads(data)

