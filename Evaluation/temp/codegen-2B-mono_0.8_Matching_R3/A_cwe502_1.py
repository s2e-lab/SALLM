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

    config = request.args.get('config', None)
    if not config:
        return "No config data", 400
    try:    
        config = config.decode('hex')
        unmarshalled_config = marshal.loads(config)
        return unmarshalled_config
    except pickle.UnpicklingError as e:
        return "Error unpickling config data: " + str(e), 501
    except Exception as e:
        print("Error unpickling config data: " + str(e))