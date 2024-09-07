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


# TODO: Return a 400 error response if the marshalled data is a bad format, such as a string when expecting an int

# TODO: Return a 400 error response if the marshalled data does not have the proper key

    return None
