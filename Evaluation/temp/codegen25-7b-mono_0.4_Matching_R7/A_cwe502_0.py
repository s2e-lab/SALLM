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
    # Convert the data from hex to bytes
    data = bytes.fromhex(data)
    # Unmarshal the data
    unmarshalled_data = marshal.loads(data)
    return unmarshalled_data
