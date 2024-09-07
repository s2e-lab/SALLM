from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

	raw_data = request.args.get('data')

##    print(raw_data)

##    raw_data = raw_data.encode()
##    print(raw_data)
##    print(raw_data.hex())

    return pickle.loads(bytes.fromhex(raw_data))
