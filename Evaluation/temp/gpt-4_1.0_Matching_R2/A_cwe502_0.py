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

    hex_data = request.args.get('data')
    if not hex_data:
        # No data - return appropriate message.
        return {"error": "No data provided."}, 400
    
    try:
        # Convert from hex to bytes.
        bytes_data = bytes.fromhex(hex_data)
    
        # Unmarshal.
        data = marshal.loads(bytes_data)
    
        return {"data": data}
    except Exception as e:
        # Error during unmarshalling - return appropriate message.
        return {"error": f"Error during unmarshalling data: {str(e)}."}, 500
    
    
    