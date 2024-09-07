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

    data = request.args.get('data')
    temp = [data[i:i + 2] for i in range(0, len(data), 2)]  # Unmarshal the marshalled data
    hex_data = '0x' + ''.join([marshal.unmarshal.dec(i) for i in temp])
    return marshal.unmarshal.dis(hex_data)

