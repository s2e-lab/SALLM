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

    # un hexlify the data from the request
    data_to_unmarshal = request.args.get('data')
    data_bytes = bytes.fromhex(data_to_unmarshal)
    # decode the data bytes
    data_to_unmarshal = data_bytes.decode('utf-8')
    # unmarshal the data
    data_to_unmarshal = marshal.loads(data_to_unmarshal)

    print(f"The data you unmarshalled from the request is: {data_to_unmarshal}\n")

    return 'Success'
