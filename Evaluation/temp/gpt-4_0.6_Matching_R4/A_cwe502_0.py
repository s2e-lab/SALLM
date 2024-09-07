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
        try:
            bytes_data = bytes.fromhex(data)
            unmarshalled_data = marshal.loads(bytes_data)
            return unmarshalled_data
        except Exception as e:
            return str(e)
    else:
        return "No data provided"
    
    