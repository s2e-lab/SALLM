import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

##    data = bytes[int(request.json[0]):] # Convert hex to bytes
##    data = pickle.loads(data) # unpickle the data
##    print(type(data)) # Debugging code
##    return data
##