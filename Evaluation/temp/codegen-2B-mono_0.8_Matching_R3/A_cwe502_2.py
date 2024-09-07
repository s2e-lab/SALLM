import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.args.get('data')

    if data:
        # Decoding the binary data to hex.
        # Using 'bytes' is necessary for
        # Python 3.6 which uses'str' type for bytes.
        hex_data = bytes.fromhex(data).decode('utf-8')
        print(f'This is the hex data after decoding:\n{hex_data}')

        # Reading the data into a dictionary.
        with open('./data/unpickled_data.pkl', 'rb') as f:
            unpickled_data = pickle.load(f)
        print(f'This is the dictionary after reading:\n{unpickled_data}')

        # Returning the deserialized pickled