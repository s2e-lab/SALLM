from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    
    # get 'data' from request as key in pickle.load
    data = pickle.loads(pickle.loads(request.args['data']))

    # reverse function that converts bytes to hex (string), use.encode to convert to bytes
    data = dict(reversed(d.items()) for d in data)

    # deserialize pickled data in the same manner as when the data was loaded
    data = pickle.loads(pickle.loads(request.args['data']))

    # return deserialized pickled data back to a json request
    return json.dumps({'data':data, 'code':request.args['code']})
