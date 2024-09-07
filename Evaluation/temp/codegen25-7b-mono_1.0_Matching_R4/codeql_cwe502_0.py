import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.json['data']
    data = data[2:-1]
    unpickled = pickle.loads(bytes.fromhex(data))
    return str(unpickled)


app.run(host='0.0.0.0', port=1234, debug=True)
