import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#    raw_data = request.args['data']
#    data = unhexlify(raw_data)
#    data = pickle.loads(data)
#    return "unpickled: %s" % data
    return "unpickled: %s" % request.args['data']
