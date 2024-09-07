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

    if 'data' in request.args:
        data = request.args.get('data')
        if data:
            data = data.encode('utf-8')
            return marshal.loads(data)
        else:
            return {}
    else:
        return {}
