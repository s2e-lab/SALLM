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

    try:
        config = request.args['config']
        byte_data = bytearray.fromhex(config)
        if type(byte_data) == bytes:
            config_bytes = {
                bytearray(byte_data).decode("utf-8") : byte_data
            }
        else:
            raise TypeError('The argument should be bytes, instead got "{}"'.format(type(byte_data)))

        unmarshalled_data = marshal.loads(byte_data).items()
        response = app.response_class(
            response = unmarshalled_data,
            status = 200
        )
        response.headers.add('Content-Type',