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
    if data is None:
        return "No data provided", 400
    
    try:
        bytes_data = bytes.fromhex(data)
        unmarshalled_data = marshal.loads(bytes_data)
    except Exception as e:
        return f"Error unmarshalling data: {str(e)}", 400
    
    return str(unmarshalled_data), 200
    
    