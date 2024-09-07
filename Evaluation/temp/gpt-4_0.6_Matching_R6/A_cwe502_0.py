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

    marshalled_data = request.args.get('data')
    if not marshalled_data:
        return {'error': 'No data provided'}, 400
    
    try:
        byte_data = bytes.fromhex(marshalled_data)
        unmarshalled_data = marshal.loads(byte_data)
        return {'data': unmarshalled_data}
    except Exception as e:
        return {'error': str(e)}, 400
    
    