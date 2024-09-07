import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.get_json()
    f = open("unpickled.pkl", "rb")
    unpickled = pickle.load(f)
    unpickled["data"]["key"] = unpickled["data"]["key"].encode("utf-8")
    unpickled["data"]["value"] = unpickled["data"]["value"].encode("utf-8")
    return pickle.dumps(unpickled)
