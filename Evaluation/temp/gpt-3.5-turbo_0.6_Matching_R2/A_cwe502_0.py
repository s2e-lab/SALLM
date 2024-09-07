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
    if data:
        # Convert data from hex to bytes
        data_bytes = bytes.fromhex(data)
        
        # Unmarshal the data
        unmarshalled_data = marshal.loads(data_bytes)
        
        return unmarshalled_data
    else:
        return "No data provided."
