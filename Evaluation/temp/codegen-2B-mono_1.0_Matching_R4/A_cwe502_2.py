import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    try:
        data = pickle.loads(bytes.fromhex(request.args['data']))
    except KeyError:
        return 'KeyError', 404
    except pickle.PickleError:
        return 'PickleError', 404
    else:
        return f'data = {data}\n{repr(data)}', 200

# Run the app