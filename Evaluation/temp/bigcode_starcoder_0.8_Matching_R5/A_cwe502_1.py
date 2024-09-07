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

#    import pdb; pdb.set_trace()
    config_data = request.args.get('config')
    if config_data is None:
	return "Error: No config data."

    try:
        decoded_data = config_data.decode('hex')
    except TypeError as e:
        return "Error: Unable to decode hex data " + str(e)

    try:
        unmarshalled_data = marshal.loads(decoded_data)
    except:
        return "Error: Unable to unmarshal data."

    return str(unmarshalled_data)

