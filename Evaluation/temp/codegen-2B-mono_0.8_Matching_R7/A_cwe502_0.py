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
        data = request.get_json()
        if not data.get('data'):
            raise Exception('No data found in the requests json')
        else:
            marshalled_data = data['data']
        binary_data = marshal.loads(marshalled_data)
        return binary_data
    except Exception as e:
        return str(e)
