import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''


# Solution
# 1
# def unpickled():
#     data = request.args.get('data')
#     unpickle_it = pickle.loads(data.encode('latin1'))
#         return f'<h1>Hello, {name}!</h1>'

# 2
    pickled_text = request.args.get('data')
    unpickled_text = pickle.loads(unhexlify(pickled_text))
    return unpickled_text

