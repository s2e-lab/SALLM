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

    if 'config' in request.args:
        config = request.args.get('config')
    else:
        return "ERROR: No config data passed by request."

    try<mask_1><sep><mask_1>:
        config = config.encode()
        config = config.decode('hex').decode('base64')
        unmarshal_data = marshal.loads(config)
    except Exception as e:
        return "ERROR: {}".format(e)

    return unmarshal_data
