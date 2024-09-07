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

    data = request.values.get('data')
    if data:
        byte_data = bytes.fromhex(data)
        unmarshalled_data = marshal.loads(byte_data)
        return unmarshalled_data
    else:
        return "Please provide marshalled data for unmarshalling."
    
    