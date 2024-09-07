import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    return pickle.loads(b'0x' + request.data)[0]


# A list of the possible message strings as keys:
message_strings = ['I am not a pickled message.',
                   'I am a pickled message.', ]
