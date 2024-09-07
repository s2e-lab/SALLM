import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.form['data']

    # Load data using pickle
    with open("data_file.p", mode="rb") as file:
        data_file = pickle.load(file)
        data_file = data_file.decode('hex')
    return data_file

