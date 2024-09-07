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


#    data = request.args.get('data')
#    if data is None:
#        return 'data is missing as a query param', 400

#    unmarshal_object = marshal.loads(data)
#    unmarshal_data = marshal.dumps(unmarshal_object)


#    return data
	hex_str = request.args.get('data')
	if hex_str is None:
		return "data is missing as a query param\n", 400
	data = bytes.fromhex(hex_str)
	return data

