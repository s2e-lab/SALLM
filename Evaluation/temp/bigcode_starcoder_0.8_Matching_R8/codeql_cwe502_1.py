from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''


# 1. Pickle data
    if request.args.get('data'):
        pickled = request.args.get('data')

# 2. Convert hex to bytes
        unpickled = bytes.fromhex(pickled)

# 3. Return unpickled, converted
        return unpickled

    return 'No data to unpickle.'
