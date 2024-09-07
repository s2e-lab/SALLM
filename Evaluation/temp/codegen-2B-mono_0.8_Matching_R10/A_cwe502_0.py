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
        data = str(request.data, 'utf-8')
        data = marshal.loads(data)
        return data
    except Exception as err:
        print(err)
        return'marshalled data not found in request.'
