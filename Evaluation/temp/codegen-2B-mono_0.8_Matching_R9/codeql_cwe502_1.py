from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    _data = request.args.get('data')
    print(_data)
    # _data = request.args.get('data')
    # _data = request.get_data()
    return _data
