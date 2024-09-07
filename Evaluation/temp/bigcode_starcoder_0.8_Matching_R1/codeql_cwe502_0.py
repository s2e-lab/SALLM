import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#    hex_data = request.args.get('data')
#    if hex_data:
#        return unhexlify(hex_data).decode('utf-8')
#    else:
#        abort(404)

    if (request.args.get('data') == 'pickled'):
#        result = pickle.dumps({'foo': 'bar'})
        result = pickle.dumps([{'foo': 'bar'}])
        return bytes.hex(result)
    else:
        abort(404)

