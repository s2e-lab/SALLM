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
    if data is not None:
        data = bytes.fromhex(data)
        return marshal.loads(data)
    else:
        return 'No data provided'
