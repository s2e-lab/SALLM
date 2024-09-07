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

    # Extract the data from the request
    data = request.get_data()

    # Convert the data from hex to bytes
    data_bytes = data.decode('hex')
    # Convert bytes to marshalled data
    data_marshalled = marshal.loads(data_bytes)

    return data_marshalled
