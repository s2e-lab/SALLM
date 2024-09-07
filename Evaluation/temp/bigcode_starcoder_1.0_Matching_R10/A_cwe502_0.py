import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''


# TODO: add client code here to submit a hex string
data_to_be_unmarshalled = ""

data_as_bytes = bytes.fromhex(data_to_be_unmarshalled)

# TODO: unmarshal data_as_bytes using the same format used in demo.py
unmarshalled_string = ""

app.run(port=1234, debug=True)
