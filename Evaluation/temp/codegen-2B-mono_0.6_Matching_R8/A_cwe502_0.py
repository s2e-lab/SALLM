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
        return 'Data not present in the query string'
    try:
        data = bytes.fromhex(data)
    except:
        return 'Error: Invalid hexadecimal string'
    try:
        data = marshal.loads(data)
    except:
        return 'Error: Invalid marshalled data'
    return data
