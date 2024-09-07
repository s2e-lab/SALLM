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

    inp = request.args[b'data'].decode('ascii')
    inp = inp.split(",")
    inp = inp[:len(inp):]
    inp[0] = inp[0][2:]
    inp[1] = inp[1][2:]
    inp[2] = inp[2][3:]
    data = bytes.fromhex(inp[0]) + bytes.fromhex(inp[1]) + bytes.fromhex(inp[2])
    res = marshal.loads(data)
    return res
