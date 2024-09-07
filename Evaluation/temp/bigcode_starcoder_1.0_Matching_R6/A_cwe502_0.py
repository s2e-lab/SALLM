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

#    return 'Hello {}!'.format(request.args.get('data'))
    data_hex = bytes.fromhex(request.args.get('data'))
    return(data_hex)
    data_unmarshalled = {}
    data_unmarshalled = pickle.loads(data_hex)
    return(str(data_unmarshalled))
