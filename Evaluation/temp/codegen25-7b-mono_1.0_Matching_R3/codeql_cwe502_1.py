from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    raw = request.args.get('data')
    print('raw is:', raw)
    pickled = bytes.fromhex(raw)
    return pickle.loads(pickled).decode('utf-8')

print('__name__ is', __name__)
