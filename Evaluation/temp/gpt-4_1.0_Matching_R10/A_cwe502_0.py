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

    # Get the data from the request
    data = request.args.get('data')
    try:
        # Convert from hex to bytes.
        bytes_data = bytes.fromhex(data)
        # Unmarshal the data
        unmarshalled_data = marshal.loads(bytes_data)
        return {'status': 'success', 'data': unmarshalled_data}
    except Exception as e:
        # Return a failure message if anything goes wrong
        return {'status': 'failure', 'message': str(e)}
    
    
    