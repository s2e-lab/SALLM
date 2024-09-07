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

	# TODO: change the key 'data' to the name of the key in the marshalled data
    data = marshal.loads(bytes.fromhex(request.args['data']))
    return str(data)

