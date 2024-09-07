import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

	pickled_hex = request.args.get('data')
	pickled = bytes.fromhex(pickled_hex)
	unpickled = pickle.loads(pickled)
	return str(unpickled) + '\n'


app.run(debug=True)