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
    if data:
        try:
            deserialized = pickle.loads(data)
            return pickle.dumps(deserialized,protocol=2)
        except:
            return 'The data in %s could not be found' % data
    return "Error: No data provided.\n"
