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


# Use pickle to generate a stream of bytes that repr(obj) can marshal.
    marshalled_bytes = pickle.dumps(config, protocol=pickle.HIGHEST_PROTOCOL)

    hex_bytes = marshalled_bytes.hex()

    unmarshalled_bytes = unhexlify(hex_bytes)

# Use the protocol 0 version of unmarshal.
    config_loaded = marshal.loads(unmarshalled_bytes)

    return (config_loaded)
