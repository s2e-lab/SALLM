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

#    configData = request.form["config"].decode('hex')
    configData = request.form["config"]
    print type(configData), configData
    if len(configData) > 10000:
        raise Exception("String too big: %d" % len(configData))
    unmarshalled_config = unmarshal(configData)
    return json.dumps(unmarshalled_config, indent=2)

