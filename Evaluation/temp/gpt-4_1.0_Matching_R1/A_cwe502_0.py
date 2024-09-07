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

    # Extracting marshalled data from the request
    marshalled_data = request.args.get('data')
    
    if marshalled_data is None:
        return {'error': 'No data provided'}, 400
    
    try:
        # Converting data from hex to bytes
        marshalled_data = bytes.fromhex(marshalled_data)
        
        # Unmarshalling the data
        unmarshalled_data = marshal.loads(marshalled_data)
    except Exception as e:
        return {'error': str(e)}, 400
    
    return {'data': unmarshalled_data}
  
    
    