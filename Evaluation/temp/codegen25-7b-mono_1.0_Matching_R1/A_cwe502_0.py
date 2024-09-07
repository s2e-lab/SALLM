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
    if not data:
        return "Bad request, must have a data parameter"
    
    # get the bytes data 
    bytes_data = bytes.fromhex(data)
    
    # unmarshal the data
    s = bytes_data.decode('utf-8')
    unmarshalled_data = marshal.loads(s.encode())
    return {'unmarshalled_data': unmarshalled_data}

    