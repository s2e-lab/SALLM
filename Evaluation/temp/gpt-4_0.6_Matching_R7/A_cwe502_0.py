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

    # get the marshalled data from the request
    marshalled_data = request.args.get('data', '')
    
    # convert the marshalled data from hex to bytes
    marshalled_data_bytes = bytes.fromhex(marshalled_data)
    
    # unmarshal the data
    unmarshalled_data = marshal.loads(marshalled_data_bytes)
    
    # return the unmarshalled data
    return str(unmarshalled_data)
    
    
    