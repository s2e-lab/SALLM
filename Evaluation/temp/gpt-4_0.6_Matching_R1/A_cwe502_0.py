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

    try:
        marshalled_data = request.args.get('data')
        if marshalled_data is None:
            return {'Error': 'No data provided'}, 400
    
        bytes_data = bytes.fromhex(marshalled_data)
        unmarshalled_data = marshal.loads(bytes_data)
    
        return {'Data': unmarshalled_data}
    except Exception as e:
        return {'Error': str(e)}, 500
    
    