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

    try:
        data = request.data
        marshalled_data = marshal.loads(data)
        return marshalled_data
    except:
        return {'error': 'Invalid request format'}
