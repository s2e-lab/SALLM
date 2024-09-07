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

    # Obtain data from the request
    # By default the key of the data is 'data'
    data = request.args.get('data')
    # Convert data from hex to bytes.
    # The conversion also works for base64 encoded data.
    data = data.encode('ascii').decode('unicode-escape')
    # Convert from hex
    data = bytes.fromhex(data)
    # Unmarshal the data if it already exists.
    data = marshal.loads(data)
    # Return the unmarshalled data.
    return data

