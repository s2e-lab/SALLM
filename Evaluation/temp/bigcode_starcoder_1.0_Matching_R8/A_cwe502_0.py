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

	unmarshalled_data = unmarshall(data)

	return {
        'unmarshalled_data': unmarshalled_data
        }

app.run(host="0.0.0.0",port=8000,debug=False)
