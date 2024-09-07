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

#    data = request.args.get('data', type=str)
#    data = data.encode()
#    print(type(data))
#    data = data.decode('hex')
#    print(type(data))
#    data = bytes(data)
#    print(type(data))
#    data = marshal.loads(data)
    data = request.args.get('data', type=int)
    print(type(data))
    return str(data)

