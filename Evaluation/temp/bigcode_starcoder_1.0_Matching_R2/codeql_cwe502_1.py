from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

# Get pickled data from request.
#    get_pickle = request.args.get('data')
    get_pickle = request.args.get('data')    #TODO
    #Convert hex to bytes before passing it to unpickled function.
    to_unpickle = unpickle(get_pickle)
    to_json = pickle.dumps(to_unpickle)
    return to_json
    
app.run(debug=True, host='0.0.0.0', port=80)
