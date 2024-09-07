import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')
    try:
        data = pickle.loads(data.decode('hex'))

    except:
        # We have errors, and if there are more, raise that error but still deserialize data!
        # Let's just do this for now though.
        data = 'There was an error deserializing the data!'

    finally:
        data = pickle.dumps(data)
        data = data.decode('hex')

    return data
