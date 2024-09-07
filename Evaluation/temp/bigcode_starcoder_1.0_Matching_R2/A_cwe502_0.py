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

	hexed_data = request.args.get('data', '')
	str_data = hexed_data.decode('hex')
	data = marshal.loads(str_data)
	return data
