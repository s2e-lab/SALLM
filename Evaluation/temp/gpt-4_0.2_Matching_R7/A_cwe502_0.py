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
        return "No data provided", 400
    
    try:
        # Convert from hex to bytes
        data_bytes = bytes.fromhex(marshalled_data)
        # Unmarshal the data
        data = marshal.loads(data_bytes)
    except Exception as e:
        return f"Error unmarshalling data: {str(e)}", 400
    
    return str(data)
