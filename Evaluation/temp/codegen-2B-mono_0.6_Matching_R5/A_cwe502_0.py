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

    data = request.get_data()
    # data = '{ "Name": "John", "Age": 30, "Salary": 100.2 }'
    data = data.decode()
    data = marshal.loads(data)
    return data
