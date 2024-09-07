import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#    print(request.form)
    string = binascii.unhexlify(request.form['data'])
    obj = pickle.loads(string)
    pickle.dump(obj, open('data/obj.pkl', 'wb'))
    return f'unpickled data: {obj}'

