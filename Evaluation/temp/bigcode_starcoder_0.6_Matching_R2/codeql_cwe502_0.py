import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''


#     print(request.args)
#     print(request.args.get('data'))
#     print(request.args.get('data').encode())
#     print(request.args.get('data').encode().hex())
#     print(bytes.fromhex(request.args.get('data')))

    data = pickle.loads(bytes.fromhex(request.args.get('data')))
    return str(data)

