import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''

    data_hex = request.args.get("data")
    data_bytes = bytes.fromhex(data_hex)
    return marshal.loads(data_bytes)
