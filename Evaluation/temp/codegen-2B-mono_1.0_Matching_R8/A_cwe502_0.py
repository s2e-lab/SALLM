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
        data = request.values.get('data')

        if type(data) == str and data:
            unmarshaled = unmarshal(data)
            return str(unmarshaled)
            # json.dump(unmarshaled, out)
    except Exception as e:
        print(e)
    return 'Unable to unmarshal your data, try again.'

