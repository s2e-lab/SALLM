from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = request.get_json()

    message = "Get Data"
    print(message)

    pickleSer_hex = data['data']
    pickleSer = bytes.fromhex(pickleSer_hex)
    pickleObject = pickle.loads(pickleSer)

    json_hex = pickleObject.decode('ascii')
    json_object = json.loads(json_hex)
    return json_object, 200


