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

    data = request.args.get('data')
    if request.method == 'POST':
        # Unmarshal data using pickle to get a list of dictionaries by the marshal module
        unmarshalled = pickle.loads(bytes.fromhex(data))
    return json.dumps(unmarshalled)
