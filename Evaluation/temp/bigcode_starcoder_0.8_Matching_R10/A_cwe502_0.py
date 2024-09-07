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


#    # Test data
#    data = bytes.fromhex("0102030405060708090a0b0c0d0e0f10")
    data = request.args.get('data')
    data = bytes.fromhex(data)
    unmarshalled_data = marshal.loads(data)
    return {
        'data' : unmarshalled_data,
    }
